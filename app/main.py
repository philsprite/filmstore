from fastapi import FastAPI
from app.api.v1.endpoints.router import router as api_router

app = FastAPI(
    title="Filmstore API",
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Filmstore API!"}

# Ganz unten: alle /api/v1-Endpunkte mounten
app.include_router(api_router)
