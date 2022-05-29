# Importing Libraries and Functionalities
from flask import Flask, render_template, request, Response, redirect, url_for
import sys
import os


# Importing Facial Recognition and Virtual Drums modules
sys.path.append(os.getcwd() + "/Face Recognition")
sys.path.append(os.getcwd() + "/Virtual Drums")

from face_rec import Capture
from virtual_drums import Drums

app = Flask(__name__)

# Code for register route for performing registration
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        cam = Capture()
        flag = cam.perform_registration()
        del cam
        return render_template('register.html', flag = flag)
    else:
        return render_template('register.html', flag = 0) # Render main registration page


# Code for login route, for performing authentication of user
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        cam = Capture()
        flag = cam.perform_login()
        if flag != 3:
            return render_template('login.html', flag = flag)
        else:
            return redirect(url_for('drums'))
    else:
        return render_template('login.html', flag = 0) # Render main login page


# Code for drums route, for user to play the drums
@app.route('/drums')
def drums():
    return render_template('drums.html')



# Used in processing of video frames (thereafter sent to register.html and login.html files)
def getVideoFaceRec(cam):
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#  Used in processing of video frames (thereafter sent to drums.html files)
def getVideoDrums(cam):
    while True:
        frame = cam.create_layout()
        yield(b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        

# Sends video frames to register.html and login.html files
@app.route('/video_face_rec')
def video_face_rec():
    return Response(getVideoFaceRec(Capture()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


# Sends video frames to drums.html file
@app.route('/video_drums')
def video_drums():
    return Response(getVideoDrums(Drums()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')



# Code for home route, for displaying the homepage of the BeatDrum app
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=6500) # Port 6500 is used
