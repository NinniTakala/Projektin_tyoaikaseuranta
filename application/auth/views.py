from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import User
from application.auth.lomakkeet import KirjautumisLomake
from application.auth.uusikayttajalomake import UusiKayttajaLomake
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


@app.route("/uusikayttaja/", methods=["GET", "POST"])
def lisaa_kayttaja():
    if request.method == "GET":
        return render_template("auth/uusikayttaja.html", form = UusiKayttajaLomake())
    form = UusiKayttajaLomake(request.form)
    
    if not form.validate():
        return render_template("auth/uusikayttaja.html", form = form)

    k = User(form.name.data,form.username.data,form.password.data)
      
    db.session().add(k)
    db.session().commit()
  
    return redirect(url_for('kirjautuminen'))
    	