from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read in details for page
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]



# Add the option to run this file directly
if __name__== "__main__":
    app.run(debug=True)