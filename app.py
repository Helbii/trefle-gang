from flask import Flask, render_template, request

from api.apiTrefle import Api
from constants import foliage, flower

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
    return render_template('searchByCaracteristics.html', foliage=foliage, flower=flower)

@app.route('/searchGrowthandCare')
def searchGrowthandInfo():
    return render_template('growthandcare.html')


@app.route('/search', methods=['POST'])
def search():
    search_results = api.get_plants_by_name(request.form['plant_name'])
    if search_results:
        return render_template('index.html', search_results=search_results)
    else:
        return render_template('index.html', message='No results found.')


@app.route("/filter", methods=['POST'])
def filter_plant():
    current_section = request.form['current_section']
    filters = {}
    if current_section == 'flower':
        if request.form.get('color'):
            filters['color'] = request.form['color']
        elif request.form.get('conspicuous'):
            filters['conspicuous'] = request.form['conspicuous']
    elif current_section == 'foliage':
        if request.form.get('texture'):
            filters['texture'] = request.form['texture']
        elif request.form.get('foliage_color'):
            filters['foliage_color'] = request.form['foliage_color']
        elif request.form.get('leaf_retention'):
            filters['leaf_retention'] = request.form['leaf_retention']
    data = api.get_plants_by_fields(filters=filters, current_section=current_section)
    if data:
        return render_template('filter.html', search_results=data["data"])
    else:
        return render_template('filter.html', message='No results found.')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
