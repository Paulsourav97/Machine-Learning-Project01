from flask import Flask
app = Flask(__name__)

@app.route("/", methods = ['Get', 'POST'])
def index():
    return "Sourav. This is my first ML project"

if __name__ == "__main__":
    app.run(debug = True)