from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://rishita:krishna1234@rishita.chiip.mongodb.net/notes"
mongo = PyMongo(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    notesinstances = list(mongo.db.notes.find().sort('_id', -1))
    return render_template('index.html', notes=notesinstances)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['txt']
        date = datetime.now().strftime("%d %b %Y")
        note = {"title" : title, "text" : text, "date": date}
        mongo.db.notes.insert_one(note)
        return redirect(url_for('home'))
    else :
        return render_template('create.html')

@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    mongo.db.notes.delete_one({'_id' : ObjectId(id)})
    return redirect(url_for('home'))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['txt']
        date = datetime.now().strftime("%d %b %Y")
        mongo.db.notes.update_one({'_id' : ObjectId(id)}, {
            "$set" : {'title': title,
                      'text' : text,
                      'date' : date}
        })
        return redirect(url_for('home'))
    else: 
        note = mongo.db.notes.find_one({'_id' : ObjectId(id)})
        return render_template('update.html', note=note)
    
if __name__ == "__main__":
    app.run(debug=True)