##leaguewebapp.py
from flask import Flask, render_template
from espnff import League

app = Flask(__name__)

@app.route("/")
def ranks():
    return render_template('index.html')

@app.route("/ranks")
def rank():
    return render_template('ranks.html',league=League(1140354, 2017).power_rankings(week=2))
  
app.run()