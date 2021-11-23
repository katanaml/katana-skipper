class MobilenetService {
    constructor() {}

    call(data) {
        const input =  JSON.parse(data);
        console.log(input);

        const response = {
            'status': 'OK'
        }

        return [JSON.stringify(response), input.task_type];
    }
}

module.exports = MobilenetService