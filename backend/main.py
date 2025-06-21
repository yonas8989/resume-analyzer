from fastapi import FastAPI
from auth import router as auth_router, create_access_token, authenticate_user
from upload import router as upload_router
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(upload_router, prefix="")

@app.post("/auth/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
async def root():
    return {"message": "Resume Analyzer API"}