from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/get-feed')
def get_feed():
    pass

@app.route('/update-queries', methods=['POST'])
def update_queries():
    print('test message')
    print(request.data)
    pass