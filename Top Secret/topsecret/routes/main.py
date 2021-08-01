from flask import Flask, render_template, redirect, url_for, session, request, Blueprint
from flask_wtf.csrf import CSRFError
from hashlib import sha512
from topsecret.models import Users

main = Blueprint('main', __name__, url_prefix='/')

@main.errorhandler(CSRFError)
def handle_csrf_error(e):
    return 'Invaild CSRF Token'

@main.errorhandler(404)
def page_not_found(e):
    return '404 Not Found', 404

@main.route('/', methods=["GET","POST"])
def index_page():
    if request.method == "GET":
        return render_template("index.html")