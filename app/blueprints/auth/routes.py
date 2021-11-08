from flask import render_template, request, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from .models import User
from flask_login import login_user, logout_user, current_user, login_required
from .import bp as auth


@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            new_user_data={
                "first_name": form.first_name.data.title(),
                "last_name": form.last_name.data.title(),
                "email": form.email.data.lower(),
                "password": form.password.data
            }
            new_user_object = User()
            new_user_object.from_dict(new_user_data)
        except:
            flash('There was an unexpected error', 'danger')
            return render_template('register.html.j2',form=form)
        flash('You Registered Successfully','success')
        return redirect(url_for('auth.login'))
    return render_template('register.html.j2',form=form)

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():        
        email = form.email.data.lower()
        password = form.password.data
        u = User.query.filter_by(email=email).first()        
        if u is not None and u.check_hashed_password(password):
            login_user(u)
            flash('You Logged in Successfully','success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid Username password combo','danger')
            return redirect(url_for('auth.login'))
    return render_template("login.html.j2", form=form)

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    if current_user is not None:
        logout_user()
        flash('You logged out','warning')
        return redirect(url_for('auth.login'))
