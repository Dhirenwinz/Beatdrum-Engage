import cv2
import pygame
import time
import handDetectionModule

# Sound track paths
top_left_path = 'Virtual Drums/drum sound/Hi-Hat-Open-Hit.mp3'
bottom_left_path = 'Virtual Drums/drum sound/Snare-Drum-Hit.wav'
center_path = 'Virtual Drums/drum sound/Kick-Drum-Hit.mp3'
bottom_right_path = 'Virtual Drums/drum sound/Floor-Tom-Drum-Hit.mp3'
top_right_path = 'Virtual Drums/drum sound/Hi-Hat-Closed-Hit.mp3'

# Initializing Hand Detector
detector = handDetectionModule.handDetector(maxHands = 2)

class Drums(object):

        # Initializing the necessary attributes
        def __init__(self):

                # Top left point coordinates of each rectangle
                self.rect1_coords = [330, 220]
                self.rect2_coords = [330, 470]
                self.rect3_coords = [680, 470]
                self.rect4_coords = [1050, 470]
                self.rect5_coords = [1050, 220]  

                # Dimensions of rectangle of each instrument in the layout
                self.rect_width = 185
                self.rect_height = 185 

                # Obtaining the top left and bottom right coordinates of each rectangle
                self.rect1_coords = self.rect1_coords + [self.rect1_coords[0] + self.rect_width, self.rect1_coords[1] + self.rect_height]
                self.rect2_coords = self.rect2_coords + [self.rect2_coords[0] + self.rect_width, self.rect2_coords[1] + self.rect_height]
                self.rect3_coords = self.rect3_coords + [self.rect3_coords[0] + self.rect_width, self.rect3_coords[1] + self.rect_height]
                self.rect4_coords = self.rect4_coords + [self.rect4_coords[0] + self.rect_width, self.rect4_coords[1] + self.rect_height]
                self.rect5_coords = self.rect5_coords + [self.rect5_coords[0] + self.rect_width, self.rect5_coords[1] + self.rect_height]

                self.time_to_sleep = 0.005 # Time delay between start and stop of an instrument's audio

                self.cap = cv2.VideoCapture(0) # Initializing the camera

                # Setting the dimensions of the window
                self.frame_width = 1500
                self.frame_height = 1000

                self.cap.set(3, self.frame_width)
                self.cap.set(4, self.frame_height)

        # Release the camera
        def __del__(self):
                self.cap.release() 

        # Plays the sound of the appropriate instrument based on the location of the index finger tips
        def play_sound(self, x, y):
                if self.rect1_coords[0] <= x <= self.rect1_coords[2] and self.rect1_coords[1] <= y <= self.rect1_coords[3]:
                        pygame.mixer.Sound(top_left_path).play()
                        time.sleep(self.time_to_sleep)
                        pygame.mixer.Sound(top_left_path).stop()

                elif self.rect2_coords[0] <= x <= self.rect2_coords[2] and self.rect2_coords[1] <= y <= self.rect2_coords[3]:
                        pygame.mixer.Sound(bottom_left_path).play()
                        time.sleep(self.time_to_sleep)
                        pygame.mixer.Sound(bottom_left_path).stop()

                elif self.rect3_coords[0] <= x <= self.rect3_coords[2] and self.rect3_coords[1] <= y <= self.rect3_coords[3]:
                        pygame.mixer.Sound(center_path).play()
                        time.sleep(self.time_to_sleep)
                        pygame.mixer.Sound(center_path).stop()

                elif self.rect4_coords[0] <= x <= self.rect4_coords[2] and self.rect4_coords[1] <= y <= self.rect4_coords[3]:
                        pygame.mixer.Sound(bottom_right_path).play()
                        time.sleep(self.time_to_sleep)
                        pygame.mixer.Sound(bottom_right_path).stop()

                elif self.rect5_coords[0] <= x <= self.rect5_coords[2] and self.rect5_coords[1] <= y <= self.rect5_coords[3]:
                        pygame.mixer.Sound(top_right_path).play()
                        time.sleep(self.time_to_sleep)
                        pygame.mixer.Sound(top_right_path).stop()


        # Creates the layout, identifies positions of hands and plays the appropriate sounds
        def create_layout(self):

                # Reading the frame
                self.is_success, frame = self.cap.read()

                # Flipping the frame to get mirror image
                frame = cv2.flip(frame, 1)
                

                #Colours
                blue = (255, 0, 0)
                yellow = (0, 255, 255)
                red = (0, 0, 255)
                green = (0, 255, 0)
                pink = (255,0,255)

                
                frame = cv2.resize(frame, (self.frame_width, self.frame_height), interpolation = cv2.INTER_AREA) # Resizing the frame

                pygame.init() # Initialize pygame


                # Creating the drum set layout
                cv2.rectangle(frame, (self.rect1_coords[0], self.rect1_coords[1]), (self.rect1_coords[2], self.rect1_coords[3]), blue, 2)
                cv2.putText(frame, "Hi Hat Open", (self.rect1_coords[0] + 7, self.rect1_coords[1] + self.rect_height // 2), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.85, color = blue, thickness = 2)

                cv2.rectangle(frame, (self.rect2_coords[0], self.rect2_coords[1]), (self.rect2_coords[2], self.rect2_coords[3]), yellow, 2)
                cv2.putText(frame, "Snare", (self.rect2_coords[0] + 45, self.rect2_coords[1] + self.rect_height // 2), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.85, color = yellow, thickness = 2)

                cv2.rectangle(frame, (self.rect3_coords[0], self.rect3_coords[1]), (self.rect3_coords[2], self.rect3_coords[3]), red, 2)
                cv2.putText(frame, "Kick", (self.rect3_coords[0] + 55, self.rect3_coords[1] + self.rect_height // 2), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.85, color = red, thickness = 2)

                cv2.rectangle(frame, (self.rect4_coords[0], self.rect4_coords[1]), (self.rect4_coords[2], self.rect4_coords[3]), green, 2)
                cv2.putText(frame, "Floor Tom Drum", (self.rect4_coords[0] + 7, self.rect4_coords[1] + self.rect_height // 2), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.85, color = green, thickness = 2)

                cv2.rectangle(frame, (self.rect5_coords[0], self.rect5_coords[1]), (self.rect5_coords[2], self.rect5_coords[3]), pink, 2)
                cv2.putText(frame, "Hi Hat Closed", (self.rect5_coords[0] + 7, self.rect5_coords[1] + self.rect_height // 2), fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 0.85, color = pink, thickness = 2)


                
                # Finding landmarks of the hands
                frame = detector.findHands(frame)
                lmList = detector.findPosition(frame)
                
                # Obtaining the landmark points of the tips of index fingers of both hands
                x1, y1, x2, y2 = 0, 0, 0, 0
                if len(lmList) != 0:
                        lemList_length = len(lmList)
                        x1, y1 = lmList[8][1:]
                        if lemList_length == 42:
                                x2, y2 = lmList[29][1:]
                
                # Locating the tips of the index fingers
                cv2.circle(frame, (x1,y1), 8, (0, 255, 255), 5)
                cv2.circle(frame, (x2,y2), 8, (0, 255, 255), 5)

                # Playing the appropriate instruments' sounds
                self.play_sound(x1, y1)
                self.play_sound(x2, y2)

                # Encoding the frame as bytestream for display on screen 
                ret, buffer = cv2.imencode('.jpg', frame)
                return buffer.tobytes()


                
