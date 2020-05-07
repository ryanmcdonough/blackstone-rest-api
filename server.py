import os
import sys

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import jsonpickle
import spacy
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from blackstone.utils.legislation_linker import extract_legislation_relations
from .Legislation import Legislation



nlp = spacy.load("en_blackstone_proto")

app = Flask(__name__)
api = Api(app)

@app.route('/legislation', methods=['POST'])
def ner():
    req_data = request.get_json()
    text = req_data['text']
                
    doc = nlp(text) 
    relations = extract_legislation_relations(doc)

    legislations = []

    for provision, provision_url, instrument, instrument_url in relations:
        legislations.append(Legislation(provision.text,provision_url,instrument.text,instrument_url))


    return jsonpickle.encode(legislations, unpicklable=False)


@app.route('/status')
def hello():
    # Render the page
    return "Working"



if __name__ == '__main__':
    app.run(host='localhost', port=4449)
