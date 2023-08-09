from flask import Flask,request,render_template
from pred import predict

app= Flask(__name__,template_folder='template')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/form",methods=["POST"])
def form():
    return render_template('form.html')

@app.route("/predict",methods = ["POST"])
def index():
    try:       
        # print('hi')
        if request.form :
            d = request.form
            d = dict(d)
            for key,value in d.items():
                d[key] = float(value)
            # print(d)
        else:
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