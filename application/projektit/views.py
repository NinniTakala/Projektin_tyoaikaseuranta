from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.projektit.models import Projekti
from application.projektit.lomakkeet import ProjektiLomake

@app.route("/projektit", methods=["GET"])
def projektit_index():
    return render_template("projektit/lista.html", projektit = Projekti.query.all())

@app.route("/projektit/new/")
@login_required
def projektit_form():
    return render_template("projektit/new.html", form = ProjektiLomake())

@app.route("/projektit/<projekti_id>/", methods=["POST"])
@login_required
def aseta_valmiiksi(projekti_id):

    t = Projekti.query.get(projekti_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("projektit_index"))
	
  
@app.route("/projektit/", methods=["POST"])
@login_required
def aloita_projekti():
    form = ProjektiLomake(request.form)
	
    if not form.validate():
        return render_template("projektit/new.html", form = form)

    t = Projekti(form.name.data)
    t.done = form.done.data
	t.account_id = current_user.id
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("projektit_index"))
	
	



  

  

	
	
	
	
	

	


