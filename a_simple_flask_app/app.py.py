import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    mean_value = None

    if request.method == 'POST':
        try:
            # Get the uploaded CSV file from the request
            uploaded_file = request.files['csv_file']
            
            # Check if a file was provided
            if uploaded_file.filename != '':
                # Read the CSV file and calculate the mean of the first column
                csv_data = csv.reader(uploaded_file)
                first_column_values = [float(row[0]) for row in csv_data]
                mean_value = sum(first_column_values) / len(first_column_values)
        except (ValueError, IndexError):
            # Handle invalid input (non-numeric values or missing data)
            mean_value = "Invalid CSV file. Please make sure it contains numeric data."

    return render_template('index.html', mean_value=mean_value)

if __name__ == '__main__':
    app.run(debug=True)