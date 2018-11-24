from flask import Flask, g, redirect, render_template, request, url_for
import sqlite3
app = Flask(__name__)

db_location = 'var/cw.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

class MysticCode:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Servants:
    def __init__(self, name, NP, Rarity, S1, S2, S3, sclass, desc):
        self.name = name
        self.NP = NP
        self.Rarity = Rarity
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        self.sclass = sclass
        self.desc = desc

@app.route('/')
def index ():
    db = get_db()
    return render_template('home.html')

@app.route('/MysticCodes')
def MysticCodes():
    MysticCodenames = []
    db = get_db()
    sql = "SELECT name FROM MysticCodes"
    for row in db.cursor().execute(sql):
        MysticCodenames.append(row[0])

    return render_template('MysticCodeList.html', names=MysticCodenames)

@app.route('/MysticCodes/<MysticCodename>')
def MysticCodename(MysticCodename):
    db = get_db()
    sql = "SELECT * FROM MysticCodes WHERE name=:name"
    result = db.cursor().execute(sql, {"name":MysticCodename}).fetchone()
    thisMysticCode = MysticCode(result[0], result[1])

    return render_template('MysticCodeDesc.html', MysticCode=thisMysticCode)


@app.route('/servants')
def servants():
    servantnames = []
    db = get_db()
    sql = "SELECT name FROM servants"
    for row in db.cursor().execute(sql):
        servantnames.append(row[0])

    return render_template('servantnames.html', names=servantnames)


@app.route('/servants/<servantname>')
def servant_name(servantname):
    db = get_db()
    sql = "SELECT * FROM servants WHERE name=:name"
    result = db.cursor().execute(sql, {"name":servantname}).fetchone()
    thisServant = Servants(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])

    return render_template('servantDesc.html', Servant=thisServant)


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        servantName = request.form['servantname']
        servantNP = request.form['NP']
        servantRarity = request.form['Rarity']
        servantS1 = request.form['S1']
        servantS2 = request.form['S2']
        servantS3 = request.form['S3']
        servantSClass = request.form['ServantClass']
        servantDesc = request.form['description']
        print(servantName, servantNP, servantRarity, servantS1, servantS2, servantS3, servantClass, servantDesc)


        db = get_db()
        sql = "INSERT INTO servants VALUES(?,?,?,?,?,?)"
        db.cursor().execute(sql,(servantName, servantS1, servantS2, servantS3, servantClass, servantDesc))
        db.commit()

        return redirect(url_for('index'))

    return render_template('input.html')
