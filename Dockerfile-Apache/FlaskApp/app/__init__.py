from flask import Flask, render_template, request, redirect, url_for, flash
import numpy as np
import hashlib
import psycopg2 
# from functions import htmlspecialchars
 
app = Flask(__name__)

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


@app.route('/inscription',methods = ['GET','POST'])
def inscription():
    name = request.cookies.get('name',default=None)                                                                                                                                                                                                                                 
    if name != None:
        return redirect(url_for("game"))
    else:
        return render_template('inscription.html')

@app.route('/connexion',methods = ['GET','POST'])
def connexion():
    return render_template('connexion.html')


@app.route('/connexion_data',methods = ['GET','POST'])
def connexion_data():
    username = htmlspecialchars(request.form.get('username'))
    mdp = htmlspecialchars(request.form.get('mdp'))
    mdp = hashlib.sha256(mdp.encode('utf-8')).hexdigest()

    cur.execute("SELECT mdp FROM test")
    data = cur.fetchall()
    is_username_in_db = np.isin(mdp, data)
    if is_username_in_db:
        return redirect(url_for("inscription_erreur",type="mdp"))

    return ""

@app.route('/game',methods = ['GET','POST'])
def game():
    return render_template('game.html')


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



@app.route('/inscription_data', methods = ['GET','POST'])  
def inscription_data():
    name = htmlspecialchars(request.form.get('name'))
    username = htmlspecialchars(request.form.get('username'))
    email = htmlspecialchars(request.form.get('mail'))
    mdp = htmlspecialchars(request.form.get('mdp'))
    mdp = hashlib.sha256(mdp.encode('utf-8')).hexdigest()

    if database_operation(name,username,email,mdp):
        cur.execute("INSERT INTO test(name,username,email,mdp) VALUES (%s,%s,%s,%s)",(name,username,email,mdp))
        conn.commit()
        return '''
        <h1>Nom: {}</h1>
        <h1>Username: {}</h1>
        <h1>Mail: {}</h1>
        <h1>Mdp: {}</h1>'''.format(name, username,email,mdp)
    return redirect(url_for("inscription"))

@app.route('/erreur/inscription', methods = ['GET','POST'])
def inscription_erreur_error():
    name = htmlspecialchars(request.form.get('name'))
    username = htmlspecialchars(request.form.get('username'))
    email = htmlspecialchars(request.form.get('mail'))
    mdp = htmlspecialchars(request.form.get('mdp'))
    mdp = hashlib.sha256(mdp.encode('utf-8')).hexdigest()

    if database_operation(name,username,email,mdp):
        cur.execute("INSERT INTO test(name,username,email,mdp) VALUES (%s,%s,%s,%s)",(name,username,email,mdp))
        conn.commit()
        return '''
        <h1>Nom: {}</h1>
        <h1>Username: {}</h1>
        <h1>Mail: {}</h1>
        <h1>Mdp: {}</h1>'''.format(name, username,email,mdp)
    return redirect(url_for("inscription"))

def database_operation(name,username,email,mdp):
    cur.execute("SELECT email FROM test")
    data = cur.fetchall()
    is_email_in_db = np.isin(email, data)
    if is_email_in_db:
        return redirect(url_for("inscription_erreur",type="email"))

    cur.execute("SELECT username FROM test")
    data = cur.fetchall()
    is_username_in_db = np.isin(username, data)
    if is_username_in_db:
        return redirect(url_for("inscription_erreur",type="username"))
    return True


@app.route('/erreur/<type>', methods = ['GET','POST'])
def inscription_erreur(type):
    return render_template('inscription.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

def htmlspecialchars(content):
    return content.replace("&", "&amp;").replace('"', "&quot;").replace("'", "&#039;").replace("<", "&lt;").replace(">", "&gt;")