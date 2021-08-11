from flask import Flask, render_template, redirect, url_for, session, request, Blueprint
from flask_wtf.csrf import CSRFError
from hashlib import sha512
from topsecret.models import db, Users

page = Blueprint('page', __name__, url_prefix='/')

@page.route('/page', methods=["GET"])
def index_page():
    if "user" in session:
        return render_template("page.html")
    else:
        return "<script>alert('로그인이 필요한 서비스입니다.'); location.href='/'; </script>"

@page.route('/page/myinfo', methods=['GET', 'POST'])
def myinfo_page():
    if "user" in session:
        if request.method == "GET":
            return render_template("mypage.html")
        else:
            new_password = request.form.get("new_pass").strip()
            repeat_password = request.form.get("repeat_pass").strip()

            if(new_password == repeat_password):
                print(session['user'])
                chk_user = Users.query.filter_by(username=session['user']).first()
                print(chk_user)

                if(result):
                    db.session.add(result)
                    db.session.commit()
                    db.session.close()
            
                    return "<script>alert('비밀번호 변경이 완료되었습니다.'); history.go(-1); </script>"
                else:
                    return "Error"

            else:
                return "Not match password"
    else:
        return "<script>alert('로그인이 필요한 서비스입니다.'); location.href='/'; </script>"