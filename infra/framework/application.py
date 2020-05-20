"""
    Facade is a structural design pattern that provides a simplified (but limited) interface to 
    a complex system of classes, library or framework.

    https://refactoring.guru/design-patterns/facade/python/example#example-0
"""

from core.port.framework.application import IApplication
from infra.framework.port.logging import Logging

class Application():

    logging : Logging = None

    def __init__(self, framework: IApplication):
        self.framework = framework

    def start(self, config: str):
        self.framework.start(config)
        logging = self.framework.logging()
    
    def router(self):
        return self.framework.router()
