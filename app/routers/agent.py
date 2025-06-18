import logging
import uuid
from fastapi import APIRouter
from pydantic import BaseModel

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/agent",
    tags=["agent"],
    responses={404: {"description": "Agent not found"}},
)


class CreateMessage(BaseModel):
    content: str


class Message(BaseModel):
    id: str
    content: str


@router.post("/", response_model=Message)
async def ask_agent(input_message: CreateMessage) -> Message:
    """
    Receives a message, logs it, and returns a standard response.
    """
    logger.info(f"Received message: '{input_message.content}'")
    message_id = str(uuid.uuid4())
    standard_response_content = (
        f"Thank you for your message: '{input_message.content}'. I have processed it."
    )

    return Message(id=message_id, content=standard_response_content)
