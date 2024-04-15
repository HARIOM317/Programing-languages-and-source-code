import React from 'react'
import './index.css';
import { CountdownCircleTimer } from "react-countdown-circle-timer";

const App = () => (
  <>
    <div>
      <CountdownCircleTimer
        isPlaying
        duration={10}
        colors={["#004777", "#F7B801", "#A30000", "#A30000"]}
        colorsTime={[10, 7, 3, 0]}
        size={150}
      >
        {({ remainingTime }) => remainingTime}
      </CountdownCircleTimer>
    </div>
  </>
);

export default App;