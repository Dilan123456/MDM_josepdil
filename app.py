from flask import Flask, request, jsonify
from flask.helpers import send_file

app = Flask(__name__, static_url_path='/', static_folder='web')

@app.route("/")
def indexPage():
     return send_file("web/index.html")  

@app.route("/square")
def square():
    # flask parameters with type and default
    n = request.args.get('n', default=1, type=int)
    # logic
    result = pow(n, 2)
    # return result as json
    return jsonify(square=result)