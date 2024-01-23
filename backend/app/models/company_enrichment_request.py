from pydantic import BaseModel

class CompanyEnrichmentRequest(BaseModel):
    pdl_id: str = None
    name: str = None
    website: str = None
    profile: str = None
