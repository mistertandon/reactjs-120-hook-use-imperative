import React, { useState, useImperativeHandle, forwardRef } from "react";

const Add = ({ param_a, param_b }, ref) => {
  const [addendA] = useState(parseFloat(param_a));
  const [addendB] = useState(parseFloat(param_b));

  const getSum = () => {
    const sum = addendA + addendB;
    console.log(`Sum: ${sum}`);
  };

  useImperativeHandle(ref, () => {
    return {
      getSum,
    };
  });
};

export default forwardRef(Add);
