from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/init-db")
def init_db():
    conn = sqlite3.connect("database.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)
    conn.close()
    return "Database created!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    conn = sqlite3.connect("database.db")
    conn.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (data["name"], data["email"], data["message"])
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved successfully!"})

if __name__ == "__main__":
    app.run()