import os

from flask import Flask, abort, request, jsonify, send_from_directory, render_template
from pyshacl import validate
import json
import rdflib
from rdflib import Graph, plugin
from rdflib.serializer import Serializer

app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')

@app.route('/foo', methods=['POST'])
def foo():
    if not request.json:
        abort(400)
    print(request.json)
    return json.dumps(request.json)


@app.route('/bar', methods=['POST'])
def bar():
    if not request.form:
        abort(400)
    print(request.form)
    return json.dumps(request.form["dg"])

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
       if request.method == 'POST':
                 dg  = request.files['datagraph']
                 sg  = request.files['shapegraph']
                 s = rdflib.Graph()
                 sr = s.parse(sg, format="ttl")
                 d = rdflib.Graph()
                 dr = d.parse(dg, format="json-ld")

                 conforms, v_graph, v_text = validate(dr, shacl_graph=sr,
                                                      data_graph_format="json-ld",
                                                      shacl_graph_format="ttl",
                                                      inference='none', debug=False,
                                                      serialize_report_graph=False)

                 return  '{} {} {}'.format(conforms, v_graph, v_text)


# TODO
# add in static file sending
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask

@app.route('/data', methods=['POST'])
def f_data():
    if request.method == "POST":
        fields = [k for k in request.form]
        values = [request.form[k] for k in request.form]
        data = dict(zip(fields, values))
        print(request.form["dg"])
        print(request.form["sg"])
    # r = validate(data_graph, shacl_graph=sg, ont_graph=og, inference='rdfs', abort_on_error=False, meta_shacl=False, debug=False)
    # conforms, results_graph, results_text = r
    return jsonify(data)

#@app.route('/')
#def hello_world():
#        return 'Tangram services are described at the GitHub Repo'
@app.route("/")
def index():
       return render_template("index.html")

if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
