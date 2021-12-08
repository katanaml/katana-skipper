const amqp = require('amqplib/callback_api');
const http = require("http");

class EventReceiver {
    constructor(username, password, host, port, queueName, serviceName) {
        this.connect_url = 'amqp://' + username + ':' + password + '@' + host + ':' + port;
        this.queueName = queueName;
        this.serviceName = serviceName;
    }

    startListener(callback, service, logger, loggerHelper) {
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
                    var r = callback(data, service, logger, queue, serviceName, msg.properties.correlationId, loggerHelper);

                    channel.sendToQueue(msg.properties.replyTo,
                        Buffer.from(r.toString()), {
                        correlationId: msg.properties.correlationId
                    });

                    channel.ack(msg);
                });
            });
        });
    }

    onRequest(data, service, logger, queue, serviceName, correlationId, loggerHelper) {
        loggerHelper(logger, queue, serviceName, correlationId, 'start', '-');

        var result = null;
        try {
            var r = service.call(data);

            loggerHelper(logger, queue, serviceName, correlationId, 'end', '-');
            console.log('Processed request: ' + r[1]);

            result = r[0];
        } catch (error) {
            const response = {
                'error': 'Receiver exception',
                'queue': queue,
                'service_name': serviceName,
                'correlation_id': correlationId
            }
            result = JSON.stringify(response);

            loggerHelper(logger, queue, serviceName, correlationId, 'end', 'Receiver exception');
            console.error("Receiver exception");
        }

        return result;
    }

    loggerHelper(logger, queue, serviceName, correlationId, taskType, description) {
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
                "task_type": taskType,
                "description": description

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
    }
}

module.exports = EventReceiver