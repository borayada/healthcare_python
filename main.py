from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    age = request.form.get("age")
    file = request.files.get("file")

    if not name or not age or not file:
        return jsonify({"error": "Missing data"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({"message": "Form submitted successfully", "name": name, "age": age, "file_path": file_path}), 200

if __name__ == "__main__":
    app.run(debug=True)
