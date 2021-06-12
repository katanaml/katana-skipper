from skipper_lib.events.event_receiver import EventReceiver
from app.training_service import TrainingService


def main():
    event_receiver = EventReceiver(username='skipper',
                                   password='welcome1',
                                   host='localhost',
                                   port=5672,
                                   queue_name='skipper_training',
                                   service=TrainingService)


if __name__ == "__main__":
    main()
