from flask import Flask, request, jsonify
from flask_cors import CORS
from face_utils import register_face, recognize_faces
from rag_chatbot import RAGChatbot
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

chatbot = RAGChatbot()

@app.route("/register", methods=["POST"])
def register():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file found"}), 400

        image = request.files['image']
        if image.filename == '':
            return jsonify({"error": "No selected image"}), 400

        if not image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return jsonify({"error": "Invalid image file type"}), 400

        name = request.form.get('name')
        if not name:
            return jsonify({"error": "Name is required"}), 400

        result = register_face(image, name)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/recognize", methods=["POST"])
def recognize():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file found"}), 400

        image = request.files['image']
        if image.filename == '':
            return jsonify({"error": "No selected image"}), 400

        if not image.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return jsonify({"error": "Invalid image file type"}), 400

        names = recognize_faces(image)
        return jsonify({"recognized": names})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        query = data.get("query", "")
        if not query:
            return jsonify({"error": "Query is required"}), 400

        response = chatbot.chat(query)
        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
