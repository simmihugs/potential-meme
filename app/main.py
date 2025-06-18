import logging
from fastapi import FastAPI
from .routers import agent
from .routers import second_agent

LOG_FORMAT = "%(levelname)s:     %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


app = FastAPI()
app.include_router(agent.router)
app.include_router(second_agent.router)
