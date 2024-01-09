from flask import Flask, render_template

app = Flask(__name__)

@app.get('/')
def home():
  return render_template("home.html")


@app.get('/projects')
def display_projects():
  return render_template("projects.html")


@app.get('/contact')
def contact():
  return render_template("contact.html")


app.run(host='0.0.0.0', port=81, debug=True)
