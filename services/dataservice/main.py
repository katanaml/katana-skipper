from skipper_lib.events.event_receiver import EventReceiver
from app.data_service import DataService
import os


def main():
    event_receiver = EventReceiver(username=os.getenv('RABBITMQ_USER'),
                                   password=os.getenv('RABBITMQ_PASSWORD'),
                                   host=os.getenv('RABBITMQ_HOST'),
                                   port=os.getenv('RABBITMQ_PORT'),
                                   queue_name=os.getenv('QUEUE_NAME'),
                                   service=DataService,
                                   service_name=os.getenv('SERVICE_NAME'),
                                   logger=os.getenv('LOGGER_RECEIVER_URL'))


if __name__ == "__main__":
    main()
