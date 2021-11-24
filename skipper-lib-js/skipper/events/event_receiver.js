const amqp = require('amqplib/callback_api');
const http = require("http");

class EventReceiver {
    constructor(username, password, host, port, queueName, serviceName) {
        this.connect_url = 'amqp://' + username + ':' + password + '@' + host + ':' + port;
        this.queueName = queueName;
        this.serviceName = serviceName;
    }

    startListener(callback, service, logger) {
        var queueName = this.queueName;
        var serviceName = this.serviceName;
        amqp.connect(this.connect_url, function (error0, connection) {
            if (error0) {
                throw error0;
            }
            connection.createChannel(function (error1, channel) {
                if (error1) {
                    throw error1;
                }
                var queue = queueName;

                channel.assertQueue(queue, {
                    durable: false
                });
                channel.prefetch(1);
                console.log('[x] Awaiting requests for: ' + serviceName + ' [x]');
                channel.consume(queue, function reply(msg) {
                    var data = msg.content.toString();
                    var r = callback(data, service, logger, queue, serviceName, msg.properties.correlationId);

                    channel.sendToQueue(msg.properties.replyTo,
                        Buffer.from(r.toString()), {
                        correlationId: msg.properties.correlationId
                    });

                    channel.ack(msg);
                });
            });
        });
    }

    onRequest(data, service, logger, queue, serviceName, correlationId) {
        if (logger !== null) {
            const postOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            };

            var requestBody = {
                "correlation_id": correlationId,
                "queue_name": queue,
                "service_name": serviceName,
                "task_type": 'start'
            };

            const req = http.request(
                logger,
                postOptions
            );

            req.on("error", (err) => {
                console.error("Logger service is not available");
            });

            req.write(JSON.stringify(requestBody));
            req.end();
        }

        var r = service.call(data);

        if (logger !== null) {
            const postOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            };

            var requestBody = {
                "correlation_id": correlationId,
                "queue_name": queue,
                "service_name": serviceName,
                "task_type": 'end'
            };

            const req = http.request(
                logger,
                postOptions
            );

            req.on("error", (err) => {
                console.error("Logger service is not available");
            });

            req.write(JSON.stringify(requestBody));
            req.end();
        }

        console.log('Processed request: ' + r[1]);

        return r[0];
    }
}

module.exports = EventReceiver