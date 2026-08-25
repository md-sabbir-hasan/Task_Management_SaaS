from fastapi import FastAPI
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Task Management API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}