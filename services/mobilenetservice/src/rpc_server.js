const amqp = require('amqplib/callback_api');
const connect_url = 'amqp://skipper:welcome1@127.0.0.1:5672';

function startReceiver() {
    amqp.connect(connect_url, function (error0, connection) {
        if (error0) {
            throw error0;
        }
        connection.createChannel(function (error1, channel) {
            if (error1) {
                throw error1;
            }
            var queue = 'rpc_queue';

            channel.assertQueue(queue, {
                durable: false
            });
            channel.prefetch(1);
            console.log(' [x] Awaiting RPC requests');
            channel.consume(queue, function reply(msg) {
                var n = parseInt(msg.content.toString());

                console.log(" [.] fib(%d)", n);

                var r = fibonacci(n);

                channel.sendToQueue(msg.properties.replyTo,
                    Buffer.from(r.toString()), {
                    correlationId: msg.properties.correlationId
                });

                channel.ack(msg);
            });
        });
    });
}

function fibonacci(n) {
    if (n === 0 || n === 1)
        return n;
    else
        return fibonacci(n - 1) + fibonacci(n - 2);
}

function main() {
    startReceiver();
}

main()