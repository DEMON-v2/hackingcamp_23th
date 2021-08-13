from topsecret.models import db
from topsecret.utils.account import create_account

def rollback_db():
    db.drop_all() # clear db
    db.create_all() # create db
    create_account()