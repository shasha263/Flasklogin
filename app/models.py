from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin
from datetime import datetime,timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4

login = LoginManager()
db= SQLAlchemy()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id= db.Column(db.String,primary_key=True)
    username=db.Column(db.String() ,  nullable =False,unique=True)
    email=db.Column(db.String() , nullable =True)
    first_name= db.Column(db.String() , nullable =True,default='')
    last_name=db.Column(db.String() , nullable =True,default='')
    password=db.Column(db.String() , nullable =False)
    created_on= db.Column(db.DateTime, nullable= False, default=datetime.now(timezone.utc))

    def __init__(self,username,email,first_name,last_name, password):
        self.username=username
        self.email=email
        self.password=generate_password_hash(password)
        self.first_name=first_name
        self.last_name=last_name
        self.id=str(uuid4())

