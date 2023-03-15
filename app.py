from flask import Flask

app = Flask(__name__)

@app.route("/") # @ is a decorator in python
def hello_world():
  return "<p>I did it...Bitch! Fuck Yeah</p>"

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)