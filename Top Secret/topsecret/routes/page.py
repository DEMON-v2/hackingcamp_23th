import re
from flask import Flask, render_template, redirect, url_for, session, request, Blueprint
from flask_wtf.csrf import CSRFError
from hashlib import sha512
from topsecret.models import db, Users

FLAG = "HCAMP{so_easy_trailing_sp2ce_w@b}"

page = Blueprint('page', __name__, url_prefix='/')

@page.route('page', methods=["GET"])
def main_page():
    if "user" in session:
        if session['user'] == "hackingcamp":
            return render_template("page.html", FLAG=FLAG)
        else:
            return render_template("page.html")
    else:
        return "<script>alert('로그인이 필요한 서비스입니다.'); location.href='/'; </script>"

@page.route('page/myinfo', methods=['GET', 'POST'])
def myinfo_page():
    if "user" in session:
        if request.method == "GET":
            return render_template("mypage.html")
        else:
            new_password = request.form.get("new_pass").strip()
            repeat_password = request.form.get("repeat_pass").strip()

            if(new_password == repeat_password):
                chk_user = Users.query.filter_by(username=session['user'].strip()).first()

                if(chk_user):
                    chk_user.password = sha512(new_password.encode()).hexdigest()
                    db.session.commit()
                    session.clear()
                    return '<script>alert("비밀번호 변경이 완료되었네요~"); location.href="page"; </script>'
            else:
                return '<script>alert("입력한 비밀번호가 서로 다릅니다."); history.go(-1); </script>'
    else:
        return "<script>alert('로그인이 필요한 서비스입니다.'); location.href='/'; </script>"

@page.route('page/logout', methods=["GET"])
def index_page():
    if "user" in session:
        session.clear()
        return redirect(url_for("main.index_page"))
    else:
        return "<script>alert('로그인이 필요한 서비스입니다.'); location.href='/'; </script>"