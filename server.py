"""
    Init API Server, here you can change framework that application is using.
"""

import os
import inject

from infra.framework.application import Application
from infra.framework.fastapi import FastAPI

framework = FastAPI()
environment = os.getenv('ENVIRONMENT', 'default')

app = Application(framework, environment)
app.start()
