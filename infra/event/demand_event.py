"""

"""
import inject

from core.port.event.event import IEvent
from core.port.event.message_queue import IMessageQueue
from core.domain.actions.demand import Demand
from infra.event.config import queue, logging

class DemandEvent(IEvent):

    demand = Demand()
    
    @queue.subscribe('demand')
    def created(self, msg):
        logging.info('Message received...')
        logging.debug(msg)
        self.demand.save(msg)

    def start():
        queue.pull()
        logging.info('Demmand events started...')
    

event = DemandEvent()
event.start()
