from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'This is the login page'


@auth.route('/sing-up')
def sing_up():
    return "this is the sing_up page"

