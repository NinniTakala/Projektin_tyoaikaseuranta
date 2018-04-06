from flask import render_template, request, redirect, url_for

from application import app
from application.auth.models import User
from application.auth.lomakkeet import KirjautumisLomake
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

@app.route("/auth/login", methods = ["GET", "POST"])
def kirjautuminen():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = KirjautumisLomake())

    form = KirjautumisLomake(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Väärä nimi tai salasana")


    login_user(user)
    return redirect(url_for("projektit_index"))  

@app.route("/auth/logout")
def ulos_kirjautuminen():
    logout_user()
    return redirect(url_for("projektit_index")) 