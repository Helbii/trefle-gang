from flask import Flask, render_template, request
from api.apiTrefle import search_plants_by_name

app = Flask(__name__)

api_token = 'R40NoI9i4IqfybCHEqFpFHD2CUcjJkOT6CZMJZgAZ5o'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    plant_name = request.form['plant_name']
    search_results = search_plants_by_name(api_token, plant_name)
    if search_results:
        return render_template('index.html', search_results=search_results)
    else:
        return render_template('index.html', message='No results found.')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
