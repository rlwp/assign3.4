from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, RUDYLEE WELCOME TO ACTIVITY 3.4!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)