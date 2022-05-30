from deepface import DeepFace
import cv2
import os


registered_users_db_path = "Face Recognition/Registered_Users"
model_name = "VGG-Face"
model = DeepFace.build_model(model_name)


#-----------REGISTER-------------#
class Capture(object):
    

    def __init__(self):
        self.cap = cv2.VideoCapture(0) # Initializing the camera
        self.permissible_distance = 0.71 # Two faces are identified as a match if the euclidean_l2 distance between them is less than this value

    # Release the camera
    def __del__(self):
        self.cap.release() 

    # To send encoded frame for display on screen 
    def get_frame(self):
        is_success, frame = self.cap.read() # Reading the frame
        frame = cv2.flip(frame, 1) # Flipping the frame to get mirror image
        ret, buffer = cv2.imencode('.jpg', frame) 
        return buffer.tobytes()
    
    # To carry out registration procedure
    def perform_registration(self):
        is_success, user_img = self.cap.read() # Reading the frame
        user_img = cv2.flip(user_img, 1) # Flipping the frame to get mirror image
 
        check_user_path = "Face Recognition/User_Check_Dummy/check_user.jpg"

        gray_img = cv2.cvtColor(user_img, cv2.COLOR_BGR2GRAY) # Converting BGR image to gray for detecting face
                
        # Detecting faces in the frame
        haar_cascade = cv2.CascadeClassifier("Face Recognition/haar_face.xml") # Haar Frontal Face Cascade Classifier is used
        faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 3) 

        flag = 0

        # No face is detected
        if len(faces_rect) == 0:
            flag = 1

        # More than one face detected
        elif len(faces_rect) > 1:
            flag = 2

        # Only one face detected, perform registration process
        else:
            cv2.imwrite(check_user_path, user_img) # Temporarily store the captured image for finding similar matches with the already registered users

            # Check for a match in the database
            df = DeepFace.find(img_path = check_user_path, db_path = registered_users_db_path, detector_backend='retinaface', 
                                                                            enforce_detection = False, distance_metric='euclidean_l2', model = model)
                
            representations_vgg_face_path = "Face Recognition/Registered_Users/representations_vgg_face.pkl"    
            
            # Remove the temporarily written captured image
            if os.path.exists(check_user_path):
                os.remove(check_user_path)

            # No match detected implying new user
            if df.head().empty:
                register_user_path = registered_users_db_path + "/register_user" + str(len(os.listdir(registered_users_db_path)) - 1) + ".jpg"
                cv2.imwrite(register_user_path, user_img)
                if os.path.exists(representations_vgg_face_path):
                    os.remove(representations_vgg_face_path)
                
                flag = 3

            else:
                distance = df.head().iat[0,1] # Distance between the captured image and the matching image

                # Match is found implying user is already registered
                if distance <= self.permissible_distance:
                    flag = 4

                # The match found is not of the current user
                else: 
                    register_user_path = registered_users_db_path + "/register_user" + str(len(os.listdir(registered_users_db_path)) - 1) + ".jpg"
                    cv2.imwrite(register_user_path, user_img) # Store the image of the user in the database
                    
                    if os.path.exists(representations_vgg_face_path):
                        os.remove(representations_vgg_face_path)
                    flag = 3
        
        
        return flag

    #-----------LOGIN-------------#

    # To carry out login procedure
    def perform_login(self):

        check_user_path = "Face Recognition/User_Check_Dummy/check_user.jpg"

        is_success, user_img = self.cap.read() # Reading the frame
        user_img = cv2.flip(user_img, 1) # Flipping the frame to get mirror image


        gray_img = cv2.cvtColor(user_img, cv2.COLOR_BGR2GRAY)  # Converting BGR image to gray for detecting face      

        # Detecting faces in the frame
        haar_cascade = cv2.CascadeClassifier("Face Recognition/haar_face.xml")
        faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 3) 

        flag = 0

        # No face is detected
        if len(faces_rect) == 0:
            flag = 1

        # More than one face detected
        elif len(faces_rect) > 1:
            flag = 2

        # Only one face detected, perform registration process
        else:    
            cv2.imwrite(check_user_path, user_img) # Temporarily store the captured image for finding similar matches with the already registered users

            df = DeepFace.find(img_path = check_user_path, db_path = registered_users_db_path, detector_backend='retinaface', 
                                                                            enforce_detection = False, distance_metric='euclidean_l2', model = model)
            
            # Remove the temporarily written captured image
            if os.path.exists(check_user_path):
                os.remove(check_user_path)

            # No match detected implying user not registered
            if df.head().empty:
                flag = 4


            else:
                distance = df.head().iat[0,1] # Distance between the captured image and the matching image

                # Match is found implying user is already registered
                if distance <= self.permissible_distance:
                    flag = 3

                # The match found is not of the current user
                else:
                    flag = 4
        
        
        return flag


