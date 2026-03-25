from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["portfolioDB"]
collection = db["contacts"]

@app.route("/")
def home():
    return "Flask backend running"

@app.route("/contact", methods=["POST"])
def contact():
    try:
        data = request.json
        collection.insert_one(data)
        return jsonify({"message": "Data saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": "Error saving data"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)