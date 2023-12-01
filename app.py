from flask import Flask,request,render_template
import requests
app=Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')
@app.route('/weatherapp',methods=['POST','GET'])
def get_weatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"
    param={
        'q':request.form.get('city'),
        'appid':request.form.get('appid'),
        'units':request.form.get('units')

    }
    #requests to get the data from url
    # request to get the data from the form
    response =requests.get(url,params=param)
    data=response.json()
    return f"data:{data}"
if __name__=='__main__':
    app.run(host="0.0.0.0",port=5002)