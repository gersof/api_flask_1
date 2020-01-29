import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Simulate database model.
books = [
    {'id': 0,
     'name': 'Josh Smith',
     'age':32
     },
    {'id': 1,
     'name': 'Mary Smith',
     'age':20
     },
    {'id': 2,
     'name': 'Jhon Anders',
     'age':30
     },
    
 
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hi</h1>
<p>It's a little test on flask!!</p>'''

#routes

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()