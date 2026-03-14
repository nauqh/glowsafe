from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import quiz, weather

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="GlowSafe Server",
    summary="Server for GlowSafe",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz.router)
app.include_router(weather.router)


@app.get("/")
def root():
    return {"message": "Root endpoint"}
