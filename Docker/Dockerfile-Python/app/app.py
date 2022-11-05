import os
from flask import Flask, render_template, request
import psycopg2 
from pymongo import MongoClient
from functions import htmlspecialchars
 
app = Flask(__name__)

# Connexion to postgres db
conn = psycopg2.connect(
        host="postgres",
        database="postgres",
        user="admin",
        password="mdp")
# Open a cursor to perform database operations (postgres)
cur = conn.cursor()

# Connexion to mongo db
client = MongoClient('localhost', 27017, username='admin', password='mdp')
db = client["ProjetNoSql"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main',methods = ['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/game',methods = ['GET','POST'])
def game():
    return render_template('game.html')


@app.route('/add',methods = ['GET','POST'])
def add():
    return render_template('add.html')

@app.route('/donate',methods = ['GET','POST'])
def donate():
    username = htmlspecialchars(request.form.get('username'))
    donate = htmlspecialchars(request.form.get('donate'))

    db.ProjetNoSql.insert_one({"username":username, "donate":donate})
    return '''
    <h1>Username: {}</h1>
    <h1>Don: {}</h1>'''.format(username,donate)



@app.route('/inscription', methods = ['GET','POST'])
def inscription():
    name = htmlspecialchars(request.form.get('name'))
    username = htmlspecialchars(request.form.get('username'))
    mail = htmlspecialchars(request.form.get('mail'))
    cur.execute("INSERT INTO test(name,username,mail) VALUES (%s,%s,%s)",(name,username,mail))
    conn.commit()
    return '''
    <h1>Nom: {}</h1>
    <h1>Username: {}</h1>
    <h1>Mail: {}</h1>'''.format(name, username,mail)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

