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
@app.route("/get_places")
def get_places():
    return render_template("places.html", places=mongo.db.places.find().sort("category_name"), categories=mongo.db.categories.find())


@app.route("/add_place")
def add_place():
    return render_template("addplace.html", categories=mongo.db.categories.find(), months=mongo.db.months.find())



@app.route("/insert_place", methods=['POST'])
def insert_place():
    places = mongo.db.places
    months = mongo.db.months
    places.insert_one(request.form.to_dict())
    months.insert_one(request.form.to_dict("months"))
    return redirect(url_for('get_places'))


@app.route("/place_cats-and_names")
def place_cats_and_names():
    return render_template(url_for('place-cats-and-names.html'))

if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

