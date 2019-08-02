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

# Add in a function that reads the local shape and returns human or machine response
# It will be method GET with ?url=URL&mode=[human,machine]&shape=[required,recommended]
@app.route('/netcheck', methods = ['GET'])
def netcheck():
        if request.method == 'GET':
            render_template("index.html") 


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
        if request.method == 'POST':
            dg  = request.files['datagraph']   # should try these too then error if not loadable to graph
            sg  = request.files['shapegraph']
            try:
                f = request.form['format']
            except:
                f = 'robot'

            # Make some graphs and parse our uploads into them
            # How does python treat errors here?   trapped by Flask?  (see note about try above)
            s = rdflib.Graph()
            sr = s.parse(sg, format="ttl")
            d = rdflib.Graph()
            dr = d.parse(dg, format="json-ld")

            # call pySHACL
            conforms, v_graph, v_text = validate(dr, shacl_graph=sr,
                data_graph_format="json-ld",
                shacl_graph_format="ttl",
                inference='none', debug=False,
                serialize_report_graph=False)

            # I default to robot, but then never both to test that  :(
            if f == 'human':
                return  '{} {}'.format(conforms, v_text)
            else:
                return  v_graph.serialize()

        if request.method == 'GET':
            render_template("index.html") 


#@app.route('/')
#def hello_world():
#        return 'Tangram services are described at the GitHub Repo'
@app.route("/")
def index():
        return render_template("index.html")

if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
