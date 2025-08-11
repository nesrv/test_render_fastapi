from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body>
        <h1>Калькулятор</h1>
        <form id="calc">
            <input type="number" id="a" placeholder="Число 1" required>
            <select id="op">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">×</option>
                <option value="divide">÷</option>
            </select>
            <input type="number" id="b" placeholder="Число 2" required>
            <button type="submit">=</button>
        </form>
        <div id="result"></div>
        <script>
        document.getElementById('calc').onsubmit = async (e) => {
            e.preventDefault();
            const a = document.getElementById('a').value;
            const b = document.getElementById('b').value;
            const op = document.getElementById('op').value;
            const res = await fetch(`/${op}/${a}/${b}`);
            const data = await res.json();
            document.getElementById('result').innerHTML = `<h2>Результат: ${data.result || data.error}</h2>`;
        }
        </script>
    </body>
    </html>
    """

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Деление на ноль"}
    return {"result": a / b}