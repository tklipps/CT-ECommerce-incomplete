from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from .import bp as main
from app.blueprints.auth.models import User
from app.blueprints.api.models import Item

@main.route('/', methods=['GET','POST'])
@login_required
def index():
    mics = Item.query.all()
    return render_template('index.html.j2', mics = mics)

@main.route('/dynamic', methods=['GET','POST'])
@login_required
def dynamic_mics():
    mics = Item.query.all()
    return render_template('dynamic.html.j2', mics = mics)

@main.route('/condenser', methods=['GET','POST'])
@login_required
def condenser_mics():
    mics = Item.query.all()
    return render_template('condenser.html.j2', mics = mics)

@main.route('/ribbon', methods=['GET','POST'])
@login_required
def ribbon_mics():
    mics = Item.query.all()
    return render_template('ribbon.html.j2', mics = mics)

@main.route('/info/<int:id>', methods=['GET','POST'])
@login_required
def mic_info(id):
    mic = Item.query.get(id)
    return render_template('mic_info.html.j2', mic = mic)