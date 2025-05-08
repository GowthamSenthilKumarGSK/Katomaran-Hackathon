import React, { useState } from 'react';
import RegisterFace from './RegisterFace';
import LiveRecognition from './LiveRecognition';

function App() {
  const [tab, setTab] = useState('register');
  return (
    <div>
      <button onClick={() => setTab('register')}>Register Face</button>
      <button onClick={() => setTab('recognize')}>Live Recognition</button>
      {tab === 'register' ? <RegisterFace /> : <LiveRecognition />}
    </div>
  );
}

export default App;
