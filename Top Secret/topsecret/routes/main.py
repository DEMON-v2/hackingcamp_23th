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

@main.route('', methods=["GET","POST"])
def index_page():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        hash_pw = sha512(password.encode()).hexdigest()

        result = Users.query.filter_by(username=username, password=hash_pw).first()

        if result:
            session['user'] = username
            return redirect(url_for("page.index_page"))
        else:
            return '<script>alert("아이디 또는 비밀번호가 올바르지 않습니다"); history.go(-1); </script>';