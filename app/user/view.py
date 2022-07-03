from flask import Blueprint, flash, redirect, render_template, session, url_for
from app.user.model import UserModel, UserDetailsModel
from app.user.form import RegisterForm, LoginForm, DeleteForm

user_blueprint = Blueprint('users', __name__, template_folder='templates')

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if UserModel.find_by_username(username=username):
            flash({
                'color': 'danger',
                'msg': f'Username {username} already taken',
            })
            return redirect(url_for('users.register'))
        user = UserModel(username=username, password=password)
        user.save()
        flash({
            'color': 'success',
            'msg': f'New user {username} created'
        })
        return redirect(url_for('users.register'))
    return render_template('user/register.html', form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = UserModel.find_by_username(username)
        if user and user.password == password:
            session['username'] = username
            return redirect(url_for('users.home'))
        flash({
            'color': 'danger',
            'msg': 'Invalid username or password'
        })
    
    return render_template('user/login.html', form=form)


@user_blueprint.route('/home', methods=['GET', 'POST'])
def home():
    if session.get('username', None) is None:
        return redirect(url_for('users.login'))
    users = UserModel.find_all()
    form = DeleteForm()

    if form.validate_on_submit():
        print('valid form')
        username = form.username.data
        user = UserModel.find_by_username(username)
        if user and session['username']!=user.username:
            user.delete()
            flash({
                'color': 'warning',
                'msg': f'User {username} deleted'
            })
            return redirect(url_for('users.home'))
        flash({
            'color': 'danger',
            'msg': f'Can not delete logged in user'
        })
    return render_template('user/home.html', users=users, form=form)

@user_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    flash({
        'color': 'primary',
        'msg': f'Logged out'
    })
    return redirect(url_for('users.login'))
