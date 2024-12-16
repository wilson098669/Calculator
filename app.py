from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    if request.method == 'POST':
        try:
            # Get user input
            number1 = float(request.form['number1'])
            number2 = float(request.form['number2'])
            operation = request.form['operation']

            # Perform the selected operation
            if operation == 'add':
                result = number1 + number2
            elif operation == 'subtract':
                result = number1 - number2
            elif operation == 'multiply':
                result = number1 * number2
            elif operation == 'divide':
                if number2 != 0:
                    result = number1 / number2
                else:
                    error = "Division by zero is not allowed."
            else:
                error = "Invalid operation selected."
        except ValueError:
            error = "Invalid input. Please enter numeric values."

    return render_template('calculator.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
