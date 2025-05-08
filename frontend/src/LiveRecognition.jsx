import React, { useRef } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

const LiveRecognition = () => {
  const webcamRef = useRef(null);

  const capture = async () => {
    const screenshot = webcamRef.current.getScreenshot();
    const blob = await (await fetch(screenshot)).blob();
    const formData = new FormData();
    formData.append('image', blob);

    const res = await axios.post('http://localhost:5000/recognize', formData);
    alert(`Detected: ${res.data.name}`);
  };

  return (
    <div>
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" />
      <button onClick={capture}>Recognize Face</button>
    </div>
  );
};

export default LiveRecognition;
