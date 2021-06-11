from skipper_lib.events.event_receiver import EventReceiver
from app.serving_service import ServingService


def main():
    event_receiver = EventReceiver(username='skipper',
                                   password='welcome1',
                                   host='localhost',
                                   port=5672,
                                   queue_name='skipper_serving',
                                   service=ServingService)


if __name__ == "__main__":
    main()
