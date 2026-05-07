from flask import Flask, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculator App</title>

        <style>
            body{
                font-family: Arial;
                background-color:#f0f8ff;
                text-align:center;
                padding-top:50px;
            }

            .box{
                width:350px;
                margin:auto;
                background:white;
                padding:30px;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;
            }

            input, select{
                width:90%;
                padding:10px;
                margin:10px;
                font-size:16px;
            }

            button{
                background:#007bff;
                color:white;
                border:none;
                padding:10px 20px;
                font-size:16px;
                border-radius:5px;
                cursor:pointer;
            }

            button:hover{
                background:#0056b3;
            }
        </style>
    </head>

    <body>

        <div class="box">

            <h2>Simple Calculator</h2>

            <form action="/calculate" method="post">

                <input type="number" name="num1" placeholder="Enter First Number" required>

                <input type="number" name="num2" placeholder="Enter Second Number" required>

                <select name="operation">

                    <option value="add">Addition</option>
                    <option value="sub">Subtraction</option>
                    <option value="mul">Multiplication</option>
                    <option value="div">Division</option>

                </select>

                <br><br>

                <button type="submit">Calculate</button>

            </form>

        </div>

    </body>
    </html>
    '''

# Calculate Route
@app.route('/calculate', methods=['POST'])
def calculate():

    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    result = 0

    if operation == "add":
        result = num1 + num2

    elif operation == "sub":
        result = num1 - num2

    elif operation == "mul":
        result = num1 * num2

    elif operation == "div":

        if num2 == 0:
            return "<h2>Division by zero is not allowed</h2>"

        result = num1 / num2

    return f'''
    <html>
    <head>
        <style>

            body{{
                font-family:Arial;
                background:#f0f8ff;
                text-align:center;
                padding-top:100px;
            }}

            .result-box{{
                background:white;
                width:300px;
                margin:auto;
                padding:30px;
                border-radius:10px;
                box-shadow:0px 0px 10px gray;
            }}

            a{{
                text-decoration:none;
                color:white;
                background:#007bff;
                padding:10px 15px;
                border-radius:5px;
            }}

        </style>
    </head>

    <body>

        <div class="result-box">

            <h1>Result = {result}</h1>

            <br>

            <a href="/">Back</a>

        </div>

    </body>
    </html>
    '''

# Run App
if __name__ == '__main__':
    app.run(debug=True)