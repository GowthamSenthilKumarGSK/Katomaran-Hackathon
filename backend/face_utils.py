import face_recognition
import numpy as np
import cv2
import os
import sqlite3
from datetime import datetime
from PIL import Image
import io

DB = "database.db"
IMG_DIR = "images/"
os.makedirs(IMG_DIR, exist_ok=True)

def save_to_db(name, encoding):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS faces
                 (name TEXT, encoding BLOB, timestamp TEXT)''')
    c.execute("INSERT INTO faces (name, encoding, timestamp) VALUES (?, ?, ?)",
              (name, encoding.tobytes(), datetime.now().isoformat()))
    conn.commit()
    conn.close()

def load_encodings():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT name, encoding FROM faces")
    data = c.fetchall()
    conn.close()
    encodings = [(name, np.frombuffer(enc)) for name, enc in data]
    return encodings

def register_face(file, name):
    image = face_recognition.load_image_file(file)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        encoding = encodings[0]
        save_to_db(name, encoding)
        # Save image
        img = Image.open(file)
        img.save(f"{IMG_DIR}{name}_{datetime.now().strftime('%H%M%S')}.jpg")
        return {"status": "success", "message": "Face registered"}
    else:
        return {"status": "fail", "message": "No face detected"}

def recognize_faces(file):
    unknown_img = face_recognition.load_image_file(file)
    unknown_encodings = face_recognition.face_encodings(unknown_img)
    known = load_encodings()
    recognized_names = []

    for unk in unknown_encodings:
        for name, known_enc in known:
            match = face_recognition.compare_faces([known_enc], unk)[0]
            if match:
                recognized_names.append(name)
    return list(set(recognized_names))
