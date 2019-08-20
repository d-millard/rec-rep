# in order to use this you must install the python package
# use "pip install flask"
from flask import Flask
app = Flask(__name__)


# function decorator
@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
