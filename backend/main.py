from fastapi import FastAPI
from datetime import timedelta
from auth import router as auth_router
from upload import router as upload_router

app = FastAPI()

# Include routers with prefixes
app.include_router(auth_router, prefix="/auth")
app.include_router(upload_router)

@app.get("/")
async def root():
    return {"message": "Resume Analyzer API"}