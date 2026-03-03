from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Bom Dia galera 2b!"

app.run()