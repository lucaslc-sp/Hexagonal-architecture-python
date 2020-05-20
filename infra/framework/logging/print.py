from infra.framework.logging.port.logging import Logging

class Print(Logging):

    def info(msg):
        print(msg)

    def debug(msg):
        print(msg)