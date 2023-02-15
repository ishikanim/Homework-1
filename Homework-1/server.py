from flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, render!</p>"

@app.route('/hi', methods=['GET'])
def hi():
  user_name = request.args.get("userName", "unknown")
  return render_template('main.html', user=user_name) 

@app.route('/api/fact', methods=['GET'])
def get_random_fact():
   return jsonify({"id": 17, "source": "my brain", "content": "flaming ranch cool hot doritoes exist."})

@app.route('/api/fact', methods=['POST'])
def upload_new_fact():
   print(request.json)
   return jsonify("ok")