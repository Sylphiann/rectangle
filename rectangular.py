from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)


def get_square_area(num):
    url = f"http://18.234.147.199:8080/function/area?sisi={num}"
    response = requests.get(url)
    result = response.json()
    result = round(result["luas"], 2)
    return result


def get_cube_area(num):
    url = f"http://54.90.162.45:8080/function/area?sisi={num}"
    response = requests.get(url)
    result = response.json()
    result = round(result["luas"], 2)
    return result


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", res1=None, res2=None, num1="", num2="")


@app.route("/square", methods=["POST"])
def calculate_square():
    num1 = request.form.get("num1", "")
    num2 = request.form.get("num2", "")
    res2 = request.form.get("res2", "")

    if num1:
        try:
            res1 = get_square_area(num1)
        except ValueError:
            res1 = "Invalid input"
    else:
        res1 = "Please enter a number"

    return render_template("index.html", res1=res1, res2=res2, num1=num1, num2=num2)


@app.route("/cube", methods=["POST"])
def calculate_cube():
    num1 = request.form.get("num1", "")
    num2 = request.form.get("num2", "")
    res1 = request.form.get("res1", "")

    if num2:
        try:
            res2 = get_cube_area(num2)
        except ValueError:
            res2 = "Invalid input"
    else:
        res2 = "Please enter a number"

    return render_template("index.html", res1=res1, res2=res2, num1=num1, num2=num2)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port)
