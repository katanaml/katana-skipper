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
                // var n = parseInt(msg.content.toString());

                var r = on_request(1);

                channel.sendToQueue(msg.properties.replyTo,
                    Buffer.from(r.toString()), {
                    correlationId: msg.properties.correlationId
                });

                channel.ack(msg);
            });
        });
    });
}

function on_request(param) {
    console.log(param);
    return 'OK';
}

function main() {
    startReceiver();
}

main()