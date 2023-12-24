from flask import Flask , jsonify , request

app = Flask(__name__)
@app.route('/test')
def hello_flask():
    print("i am your first api")
    return 'hello python'
    

