from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://rishita:krishna1234@rishita.chiip.mongodb.net/notesapp"
mongo = PyMongo(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    notesinstances = mongo.db.notes.find()
    return render_template('index.html', notes=notesinstances)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        note = request.form()
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)