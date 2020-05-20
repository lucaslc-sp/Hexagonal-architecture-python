'''
    Generates the fake data for demands.

    This can representes a process that recorder data about clicks/searches from 
    a website (ecommerce, social media and etc) and publish on message broker.
'''
import json
import random
import pika

from datetime import datetime
from faker import Faker

class FakeData():

    def __init__(self):
        self.fake = Faker(['pt_BR'])
        self.data = []

    def dispatch_view_messages(self):
        for _ in range(1000):
            lat_long = self.fake.local_latlng(country_code='BR')

            self.data.append({
                'product':  {
                    'id': self.fake.random_number(digits=6, fix_len=True),
                    'name': self.fake.sentence(nb_words=3)
                },
                'customer': {
                    'id': self.fake.lexify(text='???????????????????'),
                    'zipCode': self.fake.postcode(),
                },
                'demandedAt': datetime.today().strftime('%Y-%m-%dT%H:%M:%S'),
                'status': 'VIEW'
            })

fake_data = FakeData()
fake_data.dispatch_view_messages()

credential_params = pika.PlainCredentials('user', 'bitnami')
connection_params = pika.ConnectionParameters(
    credentials=credential_params)

connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='hexagonal')

for body in fake_data.data:
    channel.basic_publish(exchange='', routing_key='hexagonal', body=json.dumps(body))

connection.close()
