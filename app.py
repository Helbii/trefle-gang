from flask import Flask, render_template, request

from api.apiTrefle import Api
from constants import specifications

app = Flask(__name__)

api = Api()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/searchByName')
def searchByName():
    return render_template('index.html')

@app.route('/searchByCaracteristics')
def searchByCaracteristics():
    return render_template('searchByCaracteristics.html', specifications=specifications)

@app.route('/search', methods=['POST'])
def search():
    search_results = api.get_plants_by_name(request.form['plant_name'])
    if search_results:
        return render_template('index.html', search_results=search_results)
    else:
        return render_template('index.html', message='No results found.')

if __name__ == "__main__":
    app.run(debug=True, port=5001)