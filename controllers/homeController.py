from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    nama = 'Jinja2'
    return render_template('index.html', nama=nama)
