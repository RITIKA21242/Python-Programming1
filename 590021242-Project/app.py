from flask import Flask, render_template, request

app = Flask(__name__)

# FUNCTIONS
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

def is_palindrome(n):
    return "Palindrome" if str(n) == str(n)[::-1] else "Not Palindrome"

def simple_interest(p, r, t):
    return (p * r * t) / 100


# ROUTES
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    operation = request.form["operation"]

    try:
        if operation == "factorial":
            num = int(request.form["num"])
            result = factorial(num)

        elif operation == "fibonacci":
            num = int(request.form["num"])
            result = fibonacci(num)

        elif operation == "prime":
            num = int(request.form["num"])
            result = is_prime(num)

        elif operation == "palindrome":
            num = int(request.form["num"])
            result = is_palindrome(num)

        elif operation == "si":
            p = float(request.form["p"])
            r = float(request.form["r"])
            t = float(request.form["t"])
            result = simple_interest(p, r, t)

        else:
            result = "Invalid Operation"

    except:
        result = "Invalid Input"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)