from src.app.admin.base import admin
from src.app.admin.config import UserAdmin


def register_all():
    admin.register_model(UserAdmin)
