from flask import Flask

app = Flask(__name__)


@app.route("/info")
def lwinfo():
	return "this is harsh"

@app.route("/phone")
def lwphone():
	return "0987654321"

app.run(host="0.0.0.0")
