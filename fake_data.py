'''
    Generates the fake data for demands.

    This can representes a process that recorder data about clicks/searches from 
    a website (ecommerce, social media and etc) and publish on message broker.
'''
import json
import random
import pika
import inject

from datetime import datetime
from faker import Faker

from core.port.event.message_queue import IMessageQueue
from infra.event.message_queue.rabbitmq import RabbitMQ

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
    
    def dispatch_added_to_cart_messages(self):
        for item in random.sample(self.data, 400):
            item['status'] = 'ADDED_TO_CART'
            self.data.append(item)
    
    def dispatch_bought_messages(self):
        for item in random.sample(self.data, 200):
            item['status'] = 'BOUGHT'
            self.data.append(item)


def config_inject(binder: inject.Binder) -> None:
        binder.bind(IMessageQueue, RabbitMQ)

@inject.autoparams()
def start(mq: IMessageQueue):
    fake_data = FakeData()
    fake_data.dispatch_view_messages()
    fake_data.dispatch_added_to_cart_messages()
    fake_data.dispatch_bought_messages()

    for body in fake_data.data:
        mq.publish(body)

inject.configure(config_inject)
start()