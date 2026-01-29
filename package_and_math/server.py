from flask import Flask, render_template, request
from Maths.mathematics import subtraction, summation, multiplication

app = Flask("Mathematics Problems Solver")

@app.route("/")
def render_index_page():
    return render_template('index.html')


@app.route('/sum')
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = summation(num1,num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route('/sub')
def sub_route(): 
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1,num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route('/mul')
def mult_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1,num2)
    if result.is_integer():
        result = int(result)
    return str(result)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)
