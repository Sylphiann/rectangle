from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_square_area(num):
    url = f"http://35.193.138.18:8080/function/area?sisi={num}"
    response = requests.get(url)
    result = response.json()
    result = round(result['luas'], 2)
    return result

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', res1=None, res2=None, num1="", num2="")

@app.route('/square', methods=['POST'])
def calculate_square():
    num1 = request.form.get('num1', "")
    num2 = request.form.get('num2', "")
    res2 = request.form.get('res2', "")
    
    if num1:
        try:
            res1 = get_square_area(num1)
        except ValueError:
            res1 = "Invalid input"
    else:
        res1 = "Please enter a number"
    
    return render_template('index.html', res1=res1, res2=res2, num1=num1, num2=num2)

@app.route('/cube', methods=['POST'])
def calculate_cube():
    num1 = request.form.get('num1', "")
    num2 = request.form.get('num2', "")
    res1 = request.form.get('res1', "")
    
    if num2:
        try:
            res2 = get_square_area(num2)
        except ValueError:
            res2 = "Invalid input"
    else:
        res2 = "Please enter a number"
    
    return render_template('index.html', res1=res1, res2=res2, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run()
