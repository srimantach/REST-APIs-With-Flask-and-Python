from flask import Flask

app = Flask(__name__)

@app.route('/')  # 'http://www.google.com/'

def home():
    return """Hello world!
     Welcome to bootcamp
     This is the first flask api tutorial. """

app.run(port=5000)

