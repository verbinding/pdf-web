from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import company_enrichment, person_identify

app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include your routers
app.include_router(company_enrichment.router)
app.include_router(person_identify.router)

@app.get("/")
async def root():
    return {"message": "PDL App Backend Running"}
