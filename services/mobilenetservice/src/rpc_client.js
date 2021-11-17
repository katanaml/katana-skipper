const amqp = require('amqplib/callback_api');
const connect_url = 'amqp://skipper:welcome1@127.0.0.1:5672';

function startProducer() {
    amqp.connect(connect_url, function (error0, connection) {
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
                var correlationId = generateUuid();
                var num = parseInt(3);

                console.log(' [x] Requesting fib(%d)', num);

                channel.consume(q.queue, function (msg) {
                    if (msg.properties.correlationId === correlationId) {
                        console.log(' [.] Got %s', msg.content.toString());
                        setTimeout(function () {
                            connection.close();
                            process.exit(0);
                        }, 500);
                    }
                }, {
                    noAck: true
                });

                channel.sendToQueue('rpc_queue',
                    Buffer.from(num.toString()), {
                    correlationId: correlationId,
                    replyTo: q.queue
                });
            });
        });
    });
}

function generateUuid() {
    return Math.random().toString() +
        Math.random().toString() +
        Math.random().toString();
}

function main() {
    startProducer();
}

main()