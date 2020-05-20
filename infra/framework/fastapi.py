from core.port.framework.application import IApplication
from infra.framework.logging.print import Print
from infra.framework.config import config

class FastAPI(IApplication):
    
    def start(config_name):
        print('Starting FastAPI ...')
        config_envs = config[config_name]

    def logging():
        return Print()