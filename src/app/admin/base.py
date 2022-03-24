from sqladmin import Admin
from src.app.main import app
from src.app.database.base import engine


admin = Admin(app, engine)
