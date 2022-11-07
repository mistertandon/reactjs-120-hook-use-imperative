import React, { useRef } from "react";
import "./Calculator.css";

import Add from "./../Add";

const Calculator = () => {
  const refCtrl = useRef();
  return (
    <>
      <h3>Calculator</h3>
      <Add ref={refCtrl} param_a="5" param_b="10" />
      <button onClick={() => refCtrl.current?.getSum()}>Get Sum</button>
    </>
  );
};

export default Calculator;
