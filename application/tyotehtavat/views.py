from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.tyotehtavat.models import Tyotehtava
from application.auth.lomakkeet import LisaaTehtavia
from application.auth.lomakkeet import MuokkaaTehtavaa
from application.auth.lomakkeet import MuokkaaKuvausta
from application.auth.lomakkeet import MuokkaaTunteja
from application.projektit.models import Projekti

@app.route("/lisaatehtavia/<projekti_id>/", methods=["GET", "POST"])
@login_required
def lisaatehtavia(projekti_id):

    if request.method == "GET":
        return render_template("tyotehtavat/lisaa_tehtavia.html", form=LisaaTehtavia(), projekti_id=projekti_id, projekti = Projekti.query.get(projekti_id))

    form = LisaaTehtavia(request.form)
    
    if not form.validate():
        return render_template("tyotehtavat/lisaa_tehtavia.html", form = form)
    
    t = Tyotehtava(form.tehtava.data, form.kuvaus.data, form.tunnit.data) 
    t.projekti_id = projekti_id 
    t.account_id = current_user.id
    
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("projektit_index"))

@app.route("/tarkastele_tehtavia/<projekti_id>/", methods=["GET"])
@login_required
def tarkastele_tehtavia(projekti_id):
    return render_template("tyotehtavat/tyotehtavat_listana.html", tyotehtavat = Tyotehtava.query.filter(Tyotehtava.projekti_id == projekti_id), projekti = Projekti.query.get(projekti_id))

    
@app.route("/poista_tehtava/<tyotehtava_id>/<projekti_id>/", methods=["POST"])
@login_required
def poista_tehtava(tyotehtava_id, projekti_id):

    t = Tyotehtava.query.get(tyotehtava_id)
    
    db.session().delete(t)
    db.session().commit()
  
    return tarkastele_tehtavia(projekti_id)
    
@app.route("/muokkaa_tehtavaa/<tyotehtava_id>/<projekti_id>/", methods=["GET", "POST"])
@login_required
def muokkaa_tehtavaa(tyotehtava_id, projekti_id):

    if request.method == "GET":
        return render_template("tyotehtavat/muokkaa_tehtavaa.html", form=MuokkaaTehtavaa(), tyotehtava_id=tyotehtava_id, projekti_id=projekti_id)

    form = MuokkaaTehtavaa(request.form)
    
    if not form.validate():
        return render_template("tyotehtavat/muokkaa_tehtavaa.html", tyotehtava_id = tyotehtava_id, form = form, projekti_id=projekti_id)
    
    t = Tyotehtava.query.get(tyotehtava_id)
    t.tehtava = form.tehtava.data
    
    db.session().commit()
  
    return tarkastele_tehtavia(projekti_id)
    
@app.route("/muokkaa_kuvausta/<tyotehtava_id>/<projekti_id>/", methods=["GET", "POST"])
@login_required
def muokkaa_kuvausta(tyotehtava_id, projekti_id):

    if request.method == "GET":
        return render_template("tyotehtavat/muokkaa_kuvausta.html", form=MuokkaaKuvausta(), tyotehtava_id=tyotehtava_id, projekti_id=projekti_id)

    form = MuokkaaKuvausta(request.form)
    
    if not form.validate():
        return render_template("tyotehtavat/muokkaa_kuvausta.html", tyotehtava_id = tyotehtava_id, form = form, projekti_id=projekti_id)
    
    t = Tyotehtava.query.get(tyotehtava_id)
    t.kuvaus = form.kuvaus.data
    
    db.session().commit()
  
    return tarkastele_tehtavia(projekti_id)
    
@app.route("/muokkaa_tunteja/<tyotehtava_id>/<projekti_id>/", methods=["GET", "POST"])
@login_required
def muokkaa_tunteja(tyotehtava_id, projekti_id):

    if request.method == "GET":
        return render_template("tyotehtavat/muokkaa_tunteja.html", form=MuokkaaTunteja(), tyotehtava_id=tyotehtava_id, projekti_id=projekti_id)

    form = MuokkaaTunteja(request.form)
    
    if not form.validate():
        return render_template("tyotehtavat/muokkaa_tunteja.html", tyotehtava_id = tyotehtava_id, form = form, projekti_id=projekti_id)
    
    t = Tyotehtava.query.get(tyotehtava_id)
    t.tunnit = form.tunnit.data

    db.session().commit()
  
    return tarkastele_tehtavia(projekti_id)