from core.port.event.message_queue import IMessageQueue

class Kafka(IMessageQueue):

    def publish():
        print('publish method kafka')

    def subscribe():
        print('subscribe method kafka')

    def pull():
        print('pull method kafka')

