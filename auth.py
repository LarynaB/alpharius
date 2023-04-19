from flask import redirect, url_for
from flask_login import LoginManager, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import app, db
from models import User

from forms import LoginForm

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        pass


def auth():
    return None