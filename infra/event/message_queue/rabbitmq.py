"""

"""
import json
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
        credential_params = pika.PlainCredentials('user', 'bitnami')
        connection_params = pika.ConnectionParameters(credentials=credential_params)
        connection = pika.BlockingConnection(connection_params)

        channel.queue_declare(queue='hello')
        channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=pull)

    def pull(ch, method, properties, body):
        print(body)

