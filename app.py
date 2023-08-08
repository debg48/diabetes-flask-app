from flask import Flask,request
from pred import predict

app= Flask(__name__)

@app.route("/diabetes",methods = ["POST"])
def index():
    try:       
        d = request.get_json()
        data=predict(d)

        return {
            'data': str(data),
            'success':True
        }

    except Exception as e: 
        print(e) 
        return {
            'message':'Error',
            'success':False
        } 
