from flask import Flask, render_template, redirect, url_for, session, request, Blueprint
from flask_wtf.csrf import CSRFError
from hashlib import sha512

page = Blueprint('page', __name__, url_prefix='/')

@page.route('/page', methods=["GET"])
def index_page():
    return render_template("page.html")