from fastapi import APIRouter, HTTPException
from ..models.person_identify_request import PersonIdentifyRequest
from peopledatalabs import PDLPY
import os

router = APIRouter()

@router.post("/person_identify")
async def person_identify(data: PersonIdentifyRequest):
    api_key = os.getenv('PDL_API_KEY')
    if not api_key:
        raise HTTPException(status_code=500, detail="API key not configured")

    client = PDLPY(api_key=api_key)
    result = client.person.identify(**data.dict(), titlecase=True, pretty=True)
    if result.ok:
        return result.json()
    else:
        raise HTTPException(status_code=result.status_code, detail=result.text)
