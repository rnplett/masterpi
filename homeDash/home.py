from flask import Flask, render_template, abort
import pandas as pd
import json

app = Flask(__name__)
basePath = '/home/pi/homeDash/'

@app.route('/')
@app.route('/home')
def home():
    # Get Directory data
    d = pd.read_csv(basePath + "data/directory.csv")
    d.columns = ["client","FullName"]

    # Add directory data to the Client data for display.
    people = pd.DataFrame(d)
    people.columns = ["Device_Count","FullName"]

    return render_template('home.html', people=json.loads(people.to_json(orient="index")))

if __name__ == '__main__':
    app.run( host='masterpi.local', port=5000, ssl_context='adhoc')
