import React, { useState } from 'react';

function Button() {

    const [text, setText] = useState('');

    const [sum, setSum] = useState(0);

    function changeHandler(e) {
        setText(e.target.value);    
    };
    
    function setValueSum(sum) {
        setSum(sum);
    }
           
       
    function calculate() {
        fetch('http://localhost:5000/calculator?calculate='+encodeURIComponent(text), {
            headers: {
                'Content-Type': 'application/json'},
            method: 'GET',
                        
        })
        .then(response => response.json())
        .then(data => setValueSum(data.result));
    }
    
    return (
    <div>
       
        <input onChange={changeHandler} type="text" />
        <h2>{sum}</h2>
        <button onClick={calculate}>Click me</button>
        </div>
    );
}
export default Button;
