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


## Installation

### 1. Clone the repository:

git clone https://github.com/GowthamSenthilKumarGSK/Katomaran-Hackathon.git
cd Katomaran-Hackathon


### 2. Backend Setup (Flask)

- Install the required Python dependencies:

pip install -r requirements.txt


- Run the Flask server:

python app.py


### 3. Frontend Setup (React)

- Navigate to the `frontend` directory:

cd frontend


- Install the required Node dependencies:

npm install


- Start the React development server:

npm start


The application should now be running at `http://localhost:3000`.

## Usage

1. **Face Registration**:
   - Visit the `/register` route to register your face for recognition.
   - Upload a photo for face registration, which will be saved in the SQLite database.

2. **Face Recognition**:
   - After registering a face, visit the `/recognize` route to verify the user's identity using webcam capture.
   - If the face is recognized, a personalized greeting will be shown.

3. **Chatbot Interaction**:
   - Interact with the chatbot through the frontend interface.
   - The chatbot will provide contextually relevant answers using the RAG-based system, augmented with external knowledge.

## Technologies Used

- **Frontend**: React
- **Backend**: Flask
- **Database**: SQLite
- **Face Recognition**: OpenCV, Face Recognition
- **Chatbot**: Facebook's `rag-token-nq` model

## Contributing

Feel free to fork this repository and contribute to improving the project. You can submit issues or pull requests for suggestions, bug fixes, or enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


