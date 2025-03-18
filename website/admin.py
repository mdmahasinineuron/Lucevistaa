from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/')
def admin_home():
    return "this is admin page"