const EventReceiver = require('@katanaml/skipper-lib-js/skipper/events/event_receiver')
const MobilenetService = require('./app/mobilenet_service.js')

var RABBITMQ_USER = process.env.RABBITMQ_USER;
if (!process.env.RABBITMQ_USER) {
    RABBITMQ_USER = 'skipper';
}
var RABBITMQ_PASSWORD = process.env.RABBITMQ_PASSWORD;
if (!process.env.RABBITMQ_PASSWORD) {
    RABBITMQ_PASSWORD = 'welcome1';
}
var RABBITMQ_HOST = process.env.RABBITMQ_HOST;
if (!process.env.RABBITMQ_HOST) {
    RABBITMQ_HOST = '127.0.0.1';
}
var RABBITMQ_PORT = process.env.RABBITMQ_PORT;
if (!process.env.RABBITMQ_PORT) {
    RABBITMQ_PORT = 5672;
}
var QUEUE_NAME = process.env.QUEUE_NAME;
if (!process.env.QUEUE_NAME) {
    QUEUE_NAME = 'skipper_mobilenet';
}
var SERVICE_NAME = process.env.SERVICE_NAME;
if (!process.env.SERVICE_NAME) {
    SERVICE_NAME = 'mobilenet';
}
var LOGGER_RECEIVER_URL = process.env.LOGGER_RECEIVER_URL;
if (!process.env.LOGGER_RECEIVER_URL) {
    LOGGER_RECEIVER_URL = 'http://127.0.0.1:5001/api/v1/skipper/logger/log_receiver';
}

function main() {
    var event_receiver = new EventReceiver(RABBITMQ_USER,
        RABBITMQ_PASSWORD,
        RABBITMQ_HOST,
        RABBITMQ_PORT,
        QUEUE_NAME,
        SERVICE_NAME);
    event_receiver.startListener(event_receiver.onRequest, new MobilenetService(), LOGGER_RECEIVER_URL, event_receiver.loggerHelper);
}

main()