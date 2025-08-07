import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Calculator</title>
  <style>
    body {
      background-color: #ffd700;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      font-family: Arial, sans-serif;
    }

    .calculator {
      background: black;
      padding: 10px;
      border-radius: 10px;
      display: grid;
      grid-template-rows: auto 1fr;
      width: 300px;
    }

    .display {
      background: #e0e0e0;
      color: black;
      font-size: 2em;
      padding: 10px;
      text-align: right;
      margin-bottom: 10px;
      position: relative;
      height: 60px;
      overflow: hidden;
    }

    .expression {
      position: absolute;
      top: 5px;
      right: 10px;
      font-size: 0.6em;
      color: #666;
      text-align: left;
    }

    .result {
      position: absolute;
      bottom: 5px;
      right: 10px;
      font-size: 1.2em;
      color: black;
    }

    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }

    .buttons button {
      padding: 20px;
      font-size: 1.5em;
      background: white;
      border: 2px solid black;
      cursor: pointer;
    }

    .buttons button:active {
      background-color: #ccc;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <div class="display">
      <div class="expression" id="expressionDisplay"></div>
      <div class="result" id="resultDisplay">00</div>
    </div>
    <div class="buttons">
      <button onclick="append('1')">1</button>
      <button onclick="append('2')">2</button>
      <button onclick="append('3')">3</button>
      <button onclick="append('+')">+</button>

      <button onclick="append('4')">4</button>
      <button onclick="append('5')">5</button>
      <button onclick="append('6')">6</button>
      <button onclick="append('-')">-</button>

      <button onclick="append('7')">7</button>
      <button onclick="append('8')">8</button>
      <button onclick="append('9')">9</button>
      <button onclick="append('÷')">÷</button>

      <button onclick="clearDisplay()">c</button>
      <button onclick="append('0')">0</button>
      <button onclick="calculate()">=</button>
      <button onclick="append('x')">x</button>
    </div>
  </div>

  <script>
    const expressionDisplay = document.getElementById('expressionDisplay');
    const resultDisplay = document.getElementById('resultDisplay');

    let expression = '';

    function append(char) {
      if (resultDisplay.innerText === '00' || resultDisplay.innerText === 'Error') {
        resultDisplay.innerText = '';
        expression = '';
        expressionDisplay.innerText = '';
      }

      expression += char;
      resultDisplay.innerText += char;
    }

    function clearDisplay() {
      expression = '';
      resultDisplay.innerText = '00';
      expressionDisplay.innerText = '';
    }

    function calculate() {
      try {
        const exprForEval = expression.replace(/x/g, '*').replace(/÷/g, '/');
        const result = eval(exprForEval);
        expressionDisplay.innerText = resultDisplay.innerText;
        resultDisplay.innerText = result;
        expression = result.toString();
      } catch {
        resultDisplay.innerText = 'Error';
        expressionDisplay.innerText = expression;
        expression = '';
      }
    }
  </script>
</body>
</html>
st.components.v1.html(calculator_html, height=700)

