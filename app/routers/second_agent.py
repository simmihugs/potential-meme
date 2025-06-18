import logging
import uuid
from fastapi import APIRouter, Response

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/kimbel",
    tags=["kimbel"],
    responses={404: {"description": "Kimbel not found"}},
)


@router.get("/")
async def ask() -> Response:
    """
    Receives a message, logs it, and returns a standard response.
    """
    content: str = "wow"
    logger.info(f"Answer: '{content}'")

    return {"answer": content}
