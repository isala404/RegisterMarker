##==============================================================================
##	██████████████████████████████████████████████████████████████████
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	█░░░░█████████░█████░░████░██████████░█████░██████████░░█████░░░░█
##	█░░░███░░░░░░░░░███░░░░██░░░███░░░░███░███░░░███░░░░███░░███░░░░░█
##	█░░░░█████████░░███░░░░██░░░█████████░░███░░░█████████░░░███░░░░░█
##	█░░░░░░░░░░░███░███░░░░██░░░███░░░░░░░░███░░░███░░███░░░░███░░░░░█
##	█░░░██████████░░░███████░░░█████░░░░░░█████░█████░░████░█████░░░░█
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	█░fb.com/isalapi | github.com/mrsupiri | linkedin.com/in/supiri░░█
##	█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
##	██████████████████████████████████████████████████████████████████
##==============================================================================

from flask import Flask, render_template, flash, request, redirect, jsonify
from data.database import database
from flask_json import FlaskJSON, JsonError, json_response
app = Flask(__name__)
json = FlaskJSON(app)

@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/mark/')
def mark():
    try:
        db = database()
        data = db.read('SELECT * FROM PrizeWinners WHERE Absent IS NULL ')
        return render_template("mark.html", data=data)
    except:
        return render_template("mark.html")

@app.route('/view/')
def view():
    try:
        step = 1
        page = 0
        db = database()
        if request.args.get('step') == None or request.args.get('page') == None:
            data = db.read('SELECT * FROM PrizeWinners')
        else:
            step = int(request.args.get('step'))
            page = int(request.args.get('page'))
            
            start = step*page
            end = step*(page+1)
            
            data = db.read('SELECT * FROM PrizeWinners')[start:end]
        return render_template("view.html", data=data, step=step, page=page)
    except:
        return render_template("view.html")
		
@app.route('/view/absents/')
def viewabsents():
    try:
        db = database()
        data = db.read('SELECT * FROM PrizeWinners WHERE Absent IS NOT NULL ORDER BY PrizeID DESC')
        return render_template("absents.html", data=data)
    except:
        return render_template("absents.html")
		
@app.route('/update/')
def update():
    try:
        db = database()
        db.write('UPDATE PrizeWinners SET Absent = 1 WHERE ID = (?)', request.args.get('id'))
        return redirect(request.referrer)
    except:
        return redirect(request.referrer)

@app.route('/fix/')
def fix():
    try:
        db = database()
        data = db.read('SELECT * FROM PrizeWinners WHERE Absent IS NOT NULL ')
        return render_template("fix.html", data=data)
    except:
        return render_template("fix.html")

@app.route('/update/fix/')
def fixupdate():
    try:
        db = database()
        db.write('UPDATE PrizeWinners SET Absent = NULL WHERE ID = (?)', request.args.get('id'))
        return redirect(request.referrer)
    except:
        return redirect(request.referrer)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
