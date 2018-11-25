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
    def __init__(self, mname, desc):
        self.mname = mname
        self.desc = desc

class Servants:
    def __init__(self, name, NP, Rarity, scost, S1, S2, S3, sclass, desc):
        self.name = name
        self.NP = NP
        self.Rarity = Rarity
        self.scost = scost
        self.S1 = S1
        self.S2 = S2
        self.S3 = S3
        self.sclass = sclass
        self.desc = desc

class CraftEssence:
    def __init__(self, cname, ccost, crarity, desc):
        self.cname = cname
        self.ccost = ccost
        self.crarity = crarity
        self.desc = desc

@app.route('/')
def index ():
    db = get_db()
    return render_template('home.html')

@app.route('/MysticCodes')
def MysticCodes():
    MysticCodenames = []
    db = get_db()
    sql = "SELECT mname FROM MysticCodes"
    for row in db.cursor().execute(sql):
        MysticCodenames.append(row[0])

    return render_template('MysticCodeList.html', mnames=MysticCodenames)

@app.route('/MysticCodes/<MysticCodename>')
def MysticCodename(MysticCodename):
    db = get_db()
    sql = "SELECT * FROM MysticCodes WHERE mname=:mname"
    result = db.cursor().execute(sql, {"mname":MysticCodename}).fetchone()
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
    thisServant = Servants(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8])

    return render_template('servantDesc.html', Servant=thisServant)


@app.route('/CraftEssences')
def CraftEssences():
    CraftEssencenames = []
    db = get_db()
    sql = "SELECT cname FROM CraftEssences"
    for row in db.cursor().execute(sql):
        CraftEssencenames.append(row[0])

    return render_template('CraftList.html', cnames=CraftEssencenames)

@app.route('/CraftEssences/<CraftEssencename>')
def CraftEssencename(CraftEssencename):
    db = get_db()
    sql = "SELECT * FROM CraftEssences WHERE cname=:cname"
    result = db.cursor().execute(sql, {"cname":CraftEssencename}).fetchone()
    thisCraftEssence = CraftEssence(result[0], result[1], result[2], result[3])

    return render_template('CraftDesc.html', CraftEssence=thisCraftEssence)

@app.route('/party')
def party():
    partyservants = []
    partyCE = []
    db = get_db()
    sql = "SELECT name FROM servants"
    csql = "SELECT cname FROM CraftEssences"
    for row in db.cursor().execute(sql):
        partyservants.append(row[0])
    for row in db.cursor().execute(csql):
        partyCE.append(row[0])

    return render_template('party.html', names=partyservants, cnames=partyCE)


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        servantName = request.form['servantname']
        servantNP = request.form['NP']
        servantRarity = request.form['Rarity']
        servantCost = request.form['scost']
        servantS1 = request.form['S1']
        servantS2 = request.form['S2']
        servantS3 = request.form['S3']
        servantSClass = request.form['sclass']
        servantDesc = request.form['desc']
        print(servantName, servantNP, servantRarity, servantCost, servantS1, servantS2, servantS3, servantSClass, servantDesc)


        db = get_db()
        sql = "INSERT INTO servants VALUES(?,?,?,?,?,?,?,?,?)"
        db.cursor().execute(sql,(servantName, servantNP, servantRarity, servantCost, servantS1, servantS2, servantS3, servantSClass, servantDesc))
        db.commit()

        return redirect(url_for('index'))

    return render_template('input.html')

@app.route('/sendCE', methods=['GET', 'POST'])
def sendCE():
    if request.method == 'POST':
        craftName = request.form['craftname']
        craftRarity = request.form['crarity']
        craftCost = request.form['ccost']
        craftDesc = request.form['cdesc']
        print(craftName, craftRarity, craftCost, craftCost, craftDesc)


        db = get_db()
        sql = "INSERT INTO CraftEssences VALUES(?,?,?,?)"
        db.cursor().execute(sql,(craftName, craftRarity, craftCost, craftDesc))
        db.commit()

        return redirect(url_for('index'))

    return render_template('inputCE.html')
