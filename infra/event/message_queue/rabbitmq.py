"""

"""

import pika
from core.port.event.message_queue import IMessageQueue

class RabbitMQ(IMessageQueue):

    def publish(msg):
        credential_params = pika.PlainCredentials('user', 'bitnami')
        connection_params = pika.ConnectionParameters(credentials=credential_params)

        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        channel.queue_declare(queue='demand')

        channel.basic_publish(exchange='', routing_key='demand', body=json.dumps(msg))
        connection.close()

    def subscribe():
        print('subscribe method rabbitmq')

    def pull():
        print('pull method rabbitmq')

