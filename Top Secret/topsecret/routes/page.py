from flask import Flask, render_template, redirect, url_for, session, request, Blueprint
from flask_wtf.csrf import CSRFError
from hashlib import sha512

page = Blueprint('page', __name__, url_prefix='/')

@page.route('/page', methods=["GET"])
def index_page():
    if "user" in session:
        print(session)
        if session['user'] == "admin":
            print("good")
        return render_template("page.html")
    else:
        return "<script>alert('로그인이 필요한 서비스입니다.'); location.href='/'; </script>";