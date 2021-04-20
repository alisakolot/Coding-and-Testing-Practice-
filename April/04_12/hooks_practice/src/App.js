import React, { useState } from "react";

// runs function only once 
// function expensiveInitialState() {
//   return 10;
// }

function App() {
  const [{count, count2}, setCount] = useState({count: 10, count2: 20});
  // setCount: you can pass in a function into it

  return (
    <div>
      <button onClick = {() => setCount(currentState => currentState.count + 1)}>
        +
        </button>
        {/* currentCount: good way to avoid raised conditions, 2 updates at the same time */}
      <div>count1: {count}</div>
      <div>count2: {count2}</div>
    </div>
  );
  
};

export default App;
