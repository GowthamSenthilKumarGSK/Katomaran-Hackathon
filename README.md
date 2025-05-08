# Katomaran Hackathon

This repository contains the implementation for my hackathon project, "Katomaran," featuring a React frontend and Flask backend. The project includes face recognition functionality, a RAG-based (Retrieval-Augmented Generation) chatbot, and image storage using SQLite. The goal of the project is to provide a seamless user experience through facial authentication and a conversational AI chatbot.

## Features

- **Face Recognition**: 
  - Uses `face_utils.py` for registering and recognizing faces.
  - Stores face images and user data in SQLite for future recognition.
  - Routes provided for face registration (`/register`) and recognition (`/recognize`).

- **RAG-Based Chatbot**: 
  - Built using the Facebook pre-trained `rag-token-nq` model.
  - Integrates with the Flask backend to provide contextual responses based on external knowledge sources.
  - Uses retrieval-augmented generation for accurate, dynamic responses.

- **Frontend**: 
  - Developed using React for a user-friendly interface.
  - Provides an intuitive design for face registration and interaction with the chatbot.


