from flask import Flask # here we import the Flask class
app = Flask(__name__) # we create an instance of the Flask class -> '__name__'

@app.route("/") # we use whats called a 'decorator' to tell Flask what URL should trigger our function
def hello():
    return "Hello World!" 

# only runs if the script is executed directly from the Python interpreter (and not used as an imported module)
if __name__ == "__main__":  

    app.debug = True # we want to get error messages
    app.run(host='0.0.0.0', port=8886) # make your endpoint publicly available 

