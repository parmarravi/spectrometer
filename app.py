from flask import Flask, render_template
from picamera import PiCamera
from glob import glob
from datetime import datetime
import os

app=Flask(__name__) #load flask module into python
path = os.path.dirname(os.path.realpath(__file__))

def get_photos():
    photo_files = glob("%s/static/photos/*.jpg" % path)
    photos = ["/static/photos/%s" % photo.split('/')[-1] for photo in photo_files]
    return sorted(photos, reverse=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capturespectra.html')
def capture():
    timestamp = datetime.now().isoformat()
    photo_path = '%s/static/photos/%s.jpg' % (path, timestamp)
    with PiCamera() as camera:
        camera.hflip = camera.vflip = True
        camera.resolution = (640, 400)
        camera.capture(photo_path)
    return render_template('capturespectra.html')


@app.route('/absorption.html')
def absorption():
    
    return render_template('absorption.html')

@app.route('/gallery.html')

def gallery():
    photos = get_photos()
    return render_template('gallery.html',photos=photos)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/view/<photo>/')
def view(photo):
    return render_template('view.html', photo=photo)


if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
