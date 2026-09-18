from flask import Flask

app = Flask(__name__)

@app.get('/hello')
def greet():
    return {"status":"success","msg":"hello"},200


app.run(host='0.0.0.0',port=5000)