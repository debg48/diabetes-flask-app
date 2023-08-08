from flask import Flask,request
from pred import predict

app= Flask(__name__)

@app.route("/predict",methods = ["POST"])
def index():
    try:       
        d = request.get_json()
        data=predict(d)

        return {
            'data': str(data),
            'success':True
        }

    except Exception as e: 
        # print(e)
        return {
            'message': str(e),
            'success':False
        } 

if __name__ == "__main__":
    app.run(debug=True)