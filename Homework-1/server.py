import json
from flask import Flask, render_template, request, jsonify, redirect
import db

app = Flask(__name__)

@app.before_first_request
def setup():
   db.setup()

@app.route("/")
def home():
    return render_template ("main.html")

@app.route("/survey")
def survey():
  return render_template("survey.html") 

@app.route("/decline")
def decline():
  return render_template("decline.html") 

@app.route("/thanks")
def thanks():
  return render_template("thanks.html") 

@app.route("/Results" , methods=['POST', 'GET'])
def result():
   if request.method == "POST":
      results = request.form
      name = results.get["nam"]
      email = results.get["email"]
      num = results.get["num"]
      select = results.get["campusFrequency "]
      recommend = results.get["recommend"]
      timestampy = 1
      print(request.form)
      db.add_result(name,email,num,select,recommend,timestampy)
      return redirect ("/api/results")


@app.route("/api/results", methods = ['GET'])
def result2():
   final_results = jsonify(db.get_final_results())
   return final_results