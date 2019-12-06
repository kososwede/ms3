import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId

mongo_client = MongoClient()
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGOURI")
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/get_places")
def get_places():
    return render_template("places.html", places=mongo.db.places.find().sort(
        "category_name"), categories=mongo.db.categories.find())


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
    return render_template("museums.html", places=mongo.db.places.find({
        'category_name': 'Museums'}))


@app.route("/parks")
def parks():
    return render_template("parks.html", places=mongo.db.places.find({
        'category_name': 'Parks'}))


@app.route("/activities")
def activities():
    return render_template("activities.html", places=mongo.db.places.find({
        'category_name': 'Activities'}))


@app.route("/fooddrink")
def fooddrink():
    return render_template("fooddrink.html", places=mongo.db.places.find({
        'category_name': 'Food & Drink'}))


@app.route("/history")
def history():
    return render_template("history.html", places=mongo.db.places.find({
        'category_name': 'History'}))


@app.route("/attractions")
def attractions():
    return render_template("attractions.html", places=mongo.db.places.find({
        'category_name': 'Attractions'}))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"), 
    port=int(os.getenv("PORT", 5000)),debug=
    False)