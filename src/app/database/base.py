from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from src.app.config import ROOT_PATH

Base = declarative_base()
engine = create_engine(
    f"sqlite:///{ROOT_PATH}/admin.db",
    connect_args={"check_same_thread": False},
)
