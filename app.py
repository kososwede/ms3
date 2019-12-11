import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env


mongo_client = MongoClient()
app = Flask(__name__)

app.config["MONGODB_NAME"] = os.environ.get("MONGODB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

# Function to load HOME page
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

# Function to load the Places page where you choose a category
@app.route("/get_places")
def get_places():
    return render_template("places.html", places=mongo.db.places.find().sort(
        "category_name"), categories=mongo.db.categories.find())

# This is the ADD PLACE function where you can add a new place to the database
@app.route("/add_place")
def add_place():
    return render_template("addplace.html", categories=mongo.db.categories.find())

#This function inserts (posts) the data that the user entered into my database
@app.route("/insert_place", methods=['POST'])
def insert_place():
    places = mongo.db.places
    places.insert_one(request.form.to_dict())
    return redirect(url_for('get_places'))

# This function loads all of the PLACES in the MUSEUM category
@app.route("/museums", methods=['GET'])
def museums():
    print("got here")
    return render_template("museums.html", places=mongo.db.places.find({
        'category_name': 'Museums'}))

# This function loads all of the PLACES in the PARKS category
@app.route("/parks")
def parks():
    return render_template("parks.html", places=mongo.db.places.find({
        'category_name': 'Parks'}))

# This function loads all of the PLACES in the ACTIVITIES category
@app.route("/activities")
def activities():
    return render_template("activities.html", places=mongo.db.places.find({
        'category_name': 'Activities'}))

# This function loads all of the PLACES in the FOOD & DRINK category
@app.route("/fooddrink")
def fooddrink():
    return render_template("fooddrink.html", places=mongo.db.places.find({
        'category_name': 'Food & Drink'}))

# This function loads all of the PLACES in the HISTORY category
@app.route("/history")
def history():
    return render_template("history.html", places=mongo.db.places.find({
        'category_name': 'History'}))

# This function loads all of the PLACES in the ATTRACTIONS category
@app.route("/attractions")
def attractions():
    return render_template("attractions.html", places=mongo.db.places.find({
        'category_name': 'Attractions'}))

# This function loads the ABOUT page
@app.route("/about")
def about():
    return render_template("about.html")

# This function loads the IMAGES page
@app.route("/images")
def images():
    return render_template("images.html")

# This function loads EDIT place page
@app.route('/edit_place/<place_id>')
def edit_place(place_id):
    the_place = mongo.db.places.find_one({'_id': ObjectId(place_id)})
    all_categories = mongo.db.categories.find()
    return render_template('editplace.html', place=the_place, categories=all_categories)

# This function UPDATES the the database 
@app.route('/update_place/<place_id>', methods=['POST'])
def update_place(place_id):
    places = mongo.db.places
    places.update({'_id': ObjectId(place_id)},
                  {
        'category_name': request.form.get('category_name'),
        'place_name': request.form.get('place_name'),
        'user_name': request.form.get('user_name'),
        'user_comments': request.form.get('user_comments'),
        'website': request.form.get('website')
    })
    return redirect(url_for('get_places'))

# This function DELETES a record 
@app.route('/delete_place/<place_id>')
def delete_place(place_id):
    mongo.db.places.remove({'_id': ObjectId(place_id)})
    return redirect(url_for('get_places'))


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", 5000)), debug=False)
