from sqladmin import ModelAdmin
from src.app.user.model import User


class UserAdmin(ModelAdmin, model=User):
    column_list = [User.id, User.name]
