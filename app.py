import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_client = MongoClient()
app = Flask(__name__)

app.config["MONGO_DBNAME"] = "things_to_do"
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-pv69c.mongodb.net/things_to_do?retryWrites=true&w=majority"
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_places")
def get_places():
    return render_template("places.html", places=mongo.db.places.find().sort("category_name"), categories=mongo.db.categories.find())


@app.route("/add_place")
def add_place():
    return render_template("addplace.html", categories=mongo.db.categories.find())


@app.route("/insert_place", methods=['POST'])
def insert_place():
    places = mongo.db.places
    places.insert_one(request.form.to_dict())
    return redirect(url_for('get_places'))


@app.route("/museums", methods=['GET'])
def museums():
    return render_template("museums.html", places=mongo.db.places.find({'category_name': 'Museums'}))


@app.route("/parks")
def parks():
    return render_template("parks.html")


@app.route("/activities")
def activities():
    return render_template("activities.html")


@app.route("/fooddrink")
def fooddrink():
    return render_template("fooddrink.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/attractions")
def attractions():
    return render_template("attractions.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

