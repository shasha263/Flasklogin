from functools import wraps
from flask import request
from flask.json import jsonify
from app.models import User

def token_required(a_function):
    @wraps(a_function)
    def decorated_function(*args, **kwargs):
        token=request.headers.get('x-access-token')
        if not token:
            return jsonify({'Access Denied': 'No API token provided-please register to use CUD routes'})
        u=User.query.filter_by(apitoken=token).first()
        if not u:
            return jsonify({'Access Denied': 'Invalid API token'})
        return a_function(*args, **kwargs)
    return decorated_function