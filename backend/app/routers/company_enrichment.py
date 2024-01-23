from fastapi import APIRouter, HTTPException
from ..models.company_enrichment_request import CompanyEnrichmentRequest
from peopledatalabs import PDLPY
import os

router = APIRouter()

@router.post("/company_enrichment")
async def company_enrichment(data: CompanyEnrichmentRequest):
    api_key = os.getenv('PDL_API_KEY')
    if not api_key:
        raise HTTPException(status_code=500, detail="API key not configured")

    client = PDLPY(api_key=api_key)
    result = client.company.enrichment(**data.dict(), pretty=True)
    if result.ok:
        return result.json()
    else:
        raise HTTPException(status_code=result.status_code, detail=result.text)
