from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, cs!'
    
    
@app.route('/register')
def register():
    return 'Ira'

@app.route('/list')
def list():
    return 'Ira'
    
    
if __name__ == "__main__":
    app.run(debug = True)