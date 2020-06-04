from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/api/add', methods=['POST'])
def add():
    r = request.json
    r_json = json.loads(r)
    a = r_json['a']
    b = r_json['b']
    response = a+b
    response_pickled = json.dumps(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/minus', methods=['POST'])
def minus():
    r = request.json
    r_json = json.loads(r)
    a = r_json['a']
    b = r_json['b']
    response = a-b
    response_pickled = json.dumps(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")



# start flask app
app.run(host="0.0.0.0", port=6000)
