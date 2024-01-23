from fastapi import FastAPI
# Adjust the import to the new path
from app.routers import company_enrichment, person_identify

app = FastAPI()

app.include_router(company_enrichment.router)
app.include_router(person_identify.router)

@app.get("/")
async def root():
    return {"message": "PDL App Backend Running"}
