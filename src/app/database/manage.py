from src.app.database.base import Base, engine
import src.app.user.model as user_model

db_model_list = [
    user_model,
]


def create_all():
    for db_model in db_model_list:
        db_model.Base.metadata.create_all(bind=engine)
