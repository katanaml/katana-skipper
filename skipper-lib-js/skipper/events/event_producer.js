const amqp = require('amqplib/callback_api');
const http = require("http");

class EventProducer {
    constructor(username, password, host, port) {
        this.connect_url = 'amqp://' + username + ':' + password + '@' + host + ':' + port;
    }

    call(processResponse, input, logger, queue, serviceName, loggerHelper) {
        amqp.connect(this.connect_url, function (error0, connection) {
            if (error0) {
                throw error0;
            }
            connection.createChannel(function (error1, channel) {
                if (error1) {
                    throw error1;
                }
                channel.assertQueue('', {
                    exclusive: true
                }, function (error2, q) {
                    if (error2) {
                        throw error2;
                    }
                    var correlationId = Math.random().toString() +
                        Math.random().toString() +
                        Math.random().toString();

                    loggerHelper(logger, queue, serviceName, correlationId, 'start', '-');

                    channel.consume(q.queue, function (msg) {
                        if (msg.properties.correlationId === correlationId) {
                            processResponse(msg.content.toString());
                            setTimeout(function () {
                                loggerHelper(logger, queue, serviceName, correlationId, 'end', '-');

                                connection.close();
                            }, 500);
                        }
                    }, {
                        noAck: true
                    });

                    channel.sendToQueue(queue,
                        Buffer.from(input), {
                        correlationId: correlationId,
                        replyTo: q.queue
                    });
                });
            });
        });
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

module.exports = EventProducer