from flask import Flask

web_app_samp = Flask(__name__)
@web_app_samp.route('/')

def index():
    return '<h1>Hello World!!</h1>'

if __name__ == "__main__":
    app.run(debug = True)
