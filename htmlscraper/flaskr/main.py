import flask
from flask import Flask, redirect, url_for, render_template,request
from flask_cors import CORS
import json
from app import query_process

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods = ['POST','GET'])
def search():
    if request.method == "POST":
        search_q = request.form.get('query')

        if not search_q:
            return render_template('error.html', message="Please provide a search query according to the format or closely resembling it.")

    # Call the query processing function
        query_data = {'search_query': search_q}
    #send query to json file
        with open('search_query.json', 'w') as outfile:
            json.dump(query_data, outfile, indent=4)        
        results = query_process()
        if not results:
            return render_template('error.html', message="No results found.")
    # get results in the new page
        return render_template('results.html', documents = results, search_query = search_q)

if __name__ == '__main__':
    app.run(debug=True)