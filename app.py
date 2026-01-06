from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "You're home now!"

@app.route("/hello-world")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)