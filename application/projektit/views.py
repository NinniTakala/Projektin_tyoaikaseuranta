from application import app, db
from flask import redirect, render_template, request, url_for
from application.projektit.models import Projekti

@app.route("/projektit", methods=["GET"])
def projektit_index():
    return render_template("projektit/lista.html", projektit = Projekti.query.all())

@app.route("/projektit/new/")
def projektit_form():
    return render_template("projektit/new.html")

@app.route("/projektit/<projekti_id>/", methods=["POST"])
def aseta_valmiiksi(projekti_id):

    t = Projekti.query.get(projekti_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("projektit_index"))
	
@app.route("/projektit/", methods=["POST"])
def aloita_projekti():
    t = Projekti(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("projektit_index"))