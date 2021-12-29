from app import app
from app.models import db, Marvel_char,User

@app.shell_context_processor
def shell_context():
    return {'db':db, 'Marvel_char':Marvel_char, 'User': User}
