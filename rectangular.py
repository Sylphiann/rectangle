from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_square_area(num):
    url = f"http://35.193.138.18:8080/function/area?sisi={num}"
    response = requests.get(url)
    result = response.json()
    result = round(result['luas'], 2)
    return result


@app.route('/',  methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getnum():
    sisi = request.form.get('number')

    if sisi:
        try:
            result = get_square_area(sisi)
        except ValueError:
            result = "Invalid input"
    else:
        result = "Please enter a number"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()