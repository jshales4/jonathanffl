##leaguewebapp.py
import os
from flask import Flask, render_template
from espnff import League

app = Flask(__name__)

@app.route("/")
def ranks():
    return render_template('index.html')

@app.route("/ranks")
def rank():
    return render_template('ranks.html',league=League(1140354, 2017).power_rankings(week=3))
  
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)