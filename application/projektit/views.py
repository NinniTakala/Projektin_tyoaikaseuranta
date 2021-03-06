from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from application import app, db
from application.projektit.models import Projekti
from application.projektit.lomakkeet import ProjektiLomake
from application.tyotehtavat.models import Tyotehtava
from application.auth.lomakkeet import KirjautumisLomake
from application.auth.lomakkeet import UusiKayttajaLomake

@app.route("/projektit", methods=["GET"])
def projektit_index():
    if current_user.is_authenticated:
        return render_template("projektit/lista.html", projektit = Projekti.query.filter(Projekti.account_id == current_user.id))
    else:
        return redirect(url_for("kirjautuminen"))      
        
@app.route("/", methods=["GET", "POST"])
def etusivu():
    if current_user.is_authenticated:
        return render_template("projektit/lista.html", projektit = Projekti.query.filter(Projekti.account_id == current_user.id))
    else:
        return redirect(url_for("kirjautuminen"))    
        

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
    t.done = False
    t.account_id = current_user.id
  
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("projektit_index"))
    
@app.route("/projektit/kesken/<projekti_id>/", methods=["POST"])
@login_required
def aseta_keskeneraiseksi(projekti_id):

    t = Projekti.query.get(projekti_id)
    t.done = False
    db.session().commit()
  
    return redirect(url_for("projektit_index"))
    
@app.route("/projektit/poista/<projekti_id>/", methods=["POST"])
@login_required
def poista(projekti_id):

    t = Projekti.query.get(projekti_id)
    
    p = Tyotehtava.query.filter(Tyotehtava.projekti_id == projekti_id)
    
    for a in p:
        db.session().delete(a)
    
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("projektit_index"))
    
@app.route('/ohjeita')
def ohjeita():
    return render_template('ohjeita.html')

    





  

  

	
	
	
	
	

	


