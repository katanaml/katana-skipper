const tfnode = require('@tensorflow/tfjs-node');
const mobilenet = require('@tensorflow-models/mobilenet');

const fs = require('fs');
const path = require('path');
const EventProducer = require('@katanaml/skipper-lib-js/skipper/events/event_producer')


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

var QUEUE_NAME_DATA = process.env.QUEUE_NAME_DATA;
if (!process.env.QUEUE_NAME_DATA) {
    QUEUE_NAME_DATA = 'skipper_data';
}
var SERVICE_NAME = process.env.SERVICE_NAME;
if (!process.env.SERVICE_NAME) {
    SERVICE_NAME = 'mobilenet';
}
var LOGGER_PRODUCER_URL = process.env.LOGGER_PRODUCER_URL;
if (!process.env.LOGGER_PRODUCER_URL) {
    LOGGER_PRODUCER_URL = 'http://127.0.0.1:5001/api/v1/skipper/logger/log_producer';
}

class MobilenetService {
    constructor() { }

    call(data) {
        const input = JSON.parse(data);
        console.log(input);

        // TFJS Node, MobileNet model
        this.runMobileNet(input.data.image);
        //

        // Sample call to verify if it works to call Python container
        // from JS container through RabbitMQ
        var event_producer = new EventProducer(
            RABBITMQ_USER,
            RABBITMQ_PASSWORD,
            RABBITMQ_HOST,
            RABBITMQ_PORT);

        var data = {
            'task_type': 'training',
            'payload': '0.2',
            'description': 'string'
        }
        data = JSON.stringify(data);
        event_producer.call(this.processResponse, data, LOGGER_PRODUCER_URL, QUEUE_NAME_DATA, SERVICE_NAME, event_producer.loggerHelper);
        //

        const response = {
            'status': 'OK'
        }

        return [JSON.stringify(response), input.task_type];
    }

    async runMobileNet(fileName) {
        // Load the image
        const imagePath = path.join(__dirname, fileName);
        const image = fs.readFileSync(imagePath);
        const decodedImage = tfnode.node.decodeImage(image, 3);

        // Load the model
        const model = await mobilenet.load();

        // Classify the image
        const predictions = await model.classify(decodedImage);

        console.log('MobileNet predictions: ');
        console.log(predictions);
    }

    processResponse(data) {
        const input = JSON.parse(data);
        console.log('Number of keys in JSON structure from Boston data service: ' + Object.keys(input).length);
    }
}

module.exports = MobilenetService