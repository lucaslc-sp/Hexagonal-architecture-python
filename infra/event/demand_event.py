"""
    An event is a message that informs various listeners about something has happened.
    It’s send by a producer which doesn’t know and doesn’t care about the consumers of the event.

    https://tuhrig.de/messages-vs-events-vs-commands/
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
