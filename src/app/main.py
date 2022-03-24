from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.database.manage import create_all

app = FastAPI()

origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
create_all()  # Create Database
from src.app.admin.manage import register_all
register_all()  # Register Admin SQLAdmin


if __name__ =="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8080)
