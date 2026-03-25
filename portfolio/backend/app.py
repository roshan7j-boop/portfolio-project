from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Connect to DB
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create table (run once)
@app.route("/init-db")
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()
    return "Database created!"

# API to store data
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    name = data["name"]
    email = data["email"]
    message = data["message"]

    conn = get_db()
    conn.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Saved successfully!"})

if __name__ == "__main__":
    if __name__ == "__main__":
        app.run()