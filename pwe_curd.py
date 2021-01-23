# upload 266
from peewee import PostgresqlDatabase
from models import User, database


def create_table():
    database.create_tables([User])


def get_user_id(username):
    user_id = User.select().where(User.username == username).get()
    print(type(user_id))
    print(user_id)
    return user_id


def is_user_exists(username):
    print('checking if user exists')
    try:
        user = User.select().where(User.username == username).get()
        print(user)
        return True
    except User.DoesNotExist:
        return False


def create_user(username, password):
    if not is_user_exists(username):
        User.create(username=username, password=password, points=0)
        user_id = get_user_id(username)
        return user_id
    else:
        return None


def add_points(username):
    AMOUNT = 5
    User.update(
        {User.points: User.points + AMOUNT}).where(
            User.username == username).execute()
    return None


def check_username_password(username, password):
    try:
        user = User.get(User.username == username, User.password == password)
        print(f'user is {user}')
        return True
    except User.DoesNotExist:
        return False


def get_users_scores():
    print('scores_table')
    users = User.select().order_by(User.points.desc()).limit(10)
    return users
