# BeatDrum

A perfect place to have fun by playing drums without the need of having actual drum kit.
It is primarily a Facial Recognition project.
<br /><br />

## Features:

- It is a desktop application that consists of two parts: Facial Recognition and Hand Recognition.
- Attractive User Interface to give the user a smooth experience.

### Facial Recognition:

- Authorization of the user is performed through facial recognition to avail the app.
- In-built DeepFace library is used for recognizing faces.

### Hand Recognition:

- Hands are recognized to facilitate the user to play the drums.
- Mediapipe library is used for detecting hands.

## How does it work?

-Consists of three sections-<br />
**Register:** Users are required to register with their face before logging and play the drums.<br />
**Login:** Users can login successfully to play the drums only after they register. <br />
**Play Drums:** Users can play drums with their hands after successfully logging in. <br />
- During both registration and login processes, if there is no face in the frame of the camera, then 'No face detected' is shown.
- During both registration and login processes, if there are more than one faces in the frame of the camera, 'More than one face detected' is shown. 
- If an already registered user tries to register again, then 'User is already registered' is shown.
- If an unregistered user tries to register, then 'Registration Successful!' is shown.
- If an unregistered user tries to login, then 'Login Unsuccessful!' is shown.
- If a registered user tries to login, then the user is redirected to the page where drums can be played.

## How to play?

Placing the index finger upright in the appropriate square of the instrument you would like to play will give you the corresponding sound.

## Setting Up:

- Download the zip file and extract the files to any directory.
- Do not change the structure of the files and folders after extracting.
- Open command line terminal in the current directory. This directory contains 'app.py' file. Install python (mine is Python 3.9.5) to run this file.
- Now, to run this file, give the command 'python app.py'.
- Once the app starts running (which is notified by 'Debugger is active!' in the terminal), open browser and enter "localhost:6500" to go to the home page of BeatDrum.<br />
  _NOTE_: Before running the file ensure that the necessary dependencies to run the app are installed on your system. If they are not installed, 'pip install' command should work to install the missing dependencies in majority of the cases. Some of the important dependencies and modules required for this app are - Flask, opencv, deepface, mediapipe, pygame, sys, os and time.
- That's it, you are good to go!


_Happy Reading_
