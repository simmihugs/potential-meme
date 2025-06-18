from fastapi import FastAPI
from .routers import agent
from .routers import second_agent

app = FastAPI()
app.include_router(agent.router)
app.include_router(second_agent.router)
