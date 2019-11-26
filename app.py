import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "things_to_do"
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-pv69c.mongodb.net/things_to_do?retryWrites=true&=majority"
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_places")
def get_places():
    return render_template("places.html", places=mongo.db.places.find())


if __name__ == "__main__":
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)