

from flask import Flask, render_template
import datetime
app=Flask(__name__) #load flask module into python

@app.route('/')

def index():
    now =datetime.datetime.now()
    timeString=now.strftime("%Y-%m-%d %H:%M:%S")
    templateData = {
        'title':'UVIspectralbench',
        'time':timeString
        }
    return render_template('index.html',**templateData)

@app.route('/capturespectra.html')

def capturespectra():

    return render_template('capturespectra.html')

@app.route('/absorption.html')

def absorption():

    return render_template('absorption.html')

@app.route('/gallery.html')

def gallery():

    return render_template('gallery.html')

@app.route('/about.html')

def about():

    return render_template('about.html')



if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
