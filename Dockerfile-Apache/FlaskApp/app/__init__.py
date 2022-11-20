from flask import Flask, render_template, request, redirect, url_for, make_response
import numpy as np
import hashlib
import psycopg2 
import redis
# from functions import htmlspecialchars

app = Flask(__name__)

redis_client = redis.Redis(
    host='redis',
    port=6379)

# Connexion to postgres db
conn = psycopg2.connect(
        host="postgres",
        database="postgres",
        user="admin",
        password="mdp")
# Open a cursor to perform database operations (postgres)
cur = conn.cursor()

@app.route('/')
def home():
    # return render_template('index.html')
    return redirect(url_for("inscription"))

#region --- INSCRIPTION ---

@app.route('/inscription',methods = ['GET','POST'])
def inscription():
    name = request.cookies.get('name',default=None)                                                                                                                                                                                                                                 
    if name != None:
        return redirect(url_for("game"))
    else:
        return render_template('inscription.html')

@app.route('/inscription_data', methods = ['GET','POST'])  
def inscription_data():
    name = htmlspecialchars(request.form.get('name'))
    username = htmlspecialchars(request.form.get('username'))
    email = htmlspecialchars(request.form.get('mail'))
    mdp = htmlspecialchars(request.form.get('mdp'))
    mdp = hashlib.sha256(mdp.encode('utf-8')).hexdigest()

    cur.execute("SELECT * FROM test WHERE email = '{}'".format(email))    
    data_m = cur.fetchall()
    if len(data_m) > 0:
        return redirect(url_for("inscription_erreur",type="email"))

    cur.execute("SELECT * FROM test WHERE username = '{}'".format(username))    
    data_u = cur.fetchall()
    if len(data_u) > 0:
        return redirect(url_for("inscription_erreur",type="username"))

    cur.execute("INSERT INTO test(name,username,email,mdp) VALUES (%s,%s,%s,%s)",(name,username,email,mdp))
    conn.commit()
    return redirect(url_for("connexion"))

@app.route('/erreur/inscription',methods = ['GET','POST'])
def inscription_redirect():
    return redirect(url_for('inscription'))

@app.route('/erreur/inscription_data', methods = ['GET','POST'])
def inscription_erreur_error():
    name = htmlspecialchars(request.form.get('name'))
    username = htmlspecialchars(request.form.get('username'))
    email = htmlspecialchars(request.form.get('mail'))
    mdp = htmlspecialchars(request.form.get('mdp'))
    mdp = hashlib.sha256(mdp.encode('utf-8')).hexdigest()

    cur.execute("SELECT * FROM test WHERE email = '{}'".format(email))    
    data_m = cur.fetchall()
    if len(data_m) > 0:
        return redirect(url_for("inscription_erreur",type="email"))

    cur.execute("SELECT * FROM test WHERE username = '{}'".format(username))    
    data_u = cur.fetchall()
    if len(data_u) > 0:
        return redirect(url_for("inscription_erreur",type="username"))

    cur.execute("INSERT INTO test(name,username,email,mdp) VALUES (%s,%s,%s,%s)",(name,username,email,mdp))
    conn.commit()
    return redirect(url_for("connexion"))

@app.route('/erreur/<type>', methods = ['GET','POST'])
def inscription_erreur(type):
    if type=="mdp":
        return render_template('connexion.html')
    else:
        return render_template('inscription.html')

#endregion

#region --- CONNEXION ---

@app.route('/connexion',methods = ['GET','POST'])
def connexion():
    return render_template('connexion.html')

@app.route('/erreur/connexion',methods = ['GET','POST'])
def connexion_redirect():
    return redirect(url_for('connexion'))

@app.route('/deconnexion',methods = ['GET','POST'])
def deconnexion():
    return render_template('deconnexion.html')

@app.route('/connexion_data',methods = ['GET','POST'])
def connexion_data():
    username = htmlspecialchars(request.form.get('username'))
    mdp = htmlspecialchars(request.form.get('mdp'))
    mdp = hashlib.sha256(mdp.encode('utf-8')).hexdigest()

    cur.execute("SELECT * FROM test WHERE username = '{}' AND mdp = '{}'".format(username,mdp))
    data = cur.fetchall()
    if len(data) > 0:
        return redirect(url_for("confirm_connexion",username=username))
    return redirect(url_for("connexion_erreur",type="mdp"))

@app.route('/confirm-<username>',methods = ['GET','POST'])
def confirm_connexion(username):
    return render_template('confirm_connexion.html')

#endregion

#region --- GAME ---

@app.route('/game',methods = ['GET','POST'])
def game():
    name = request.cookies.get('name',default=None)
    if name != None:
        jetons = redis_client.get(name)
        if jetons == None:
            jetons = "100"
            redis_client.set(name,jetons)
        resp = make_response(render_template("game.html"))
        resp.set_cookie('ckitonbjt-v2',jetons)
        return resp        
        return render_template("game.html")
    else:
        return redirect(url_for('inscription'))

@app.route("/resetJetons/<name>", methods = ['GET'])
def resetJetons(name):
    jetons = request.cookies.get('ckitonbjt-v2',default=None)
    redis_client.set(name,jetons)
    return redirect(url_for('game'))


@app.route('/add',methods = ['GET','POST'])
def add():
    return render_template('add.html')

# @app.route('/donate',methods = ['GET','POST'])
# def donate():
#     username = htmlspecialchars(request.form.get('username'))
#     donate = htmlspecialchars(request.form.get('donate'))
#     return '''
#     <h1>Username: {}</h1>
#     <h1>Don: {}</h1>'''.format(username,donate)

#endregion

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

def htmlspecialchars(content):
    return content.replace("&", "&amp;").replace('"', "&quot;").replace("'", "&#039;").replace("<", "&lt;").replace(">", "&gt;")