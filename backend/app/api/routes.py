
from fastapi import APIRouter, HTTPException
from groq import APIError

from app.schemas.ask import AskRequest, AskResponse
from app.services.llm_service import generate_answer

import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/")
def root():
    return {"message": "Hello from our API router"}


@router.post("/api/v1/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    try:
        answer = generate_answer(request.question)

        return AskResponse(
            question=request.question,
            answer=answer
        )

    except APIError:
        raise HTTPException(
            status_code=502,
            detail="The AI service is temporarily unavailable. Please try again."
        )
    except Exception:
        logger.exception("Unexpected error while processing question")
        raise HTTPException(
            status_code=500,
            detail="Something went wrong. Please try again."
        )
