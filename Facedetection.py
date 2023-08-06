#Importing required modules
import cv2
import mediapipe as mp

#Define cam as webcam
cam = cv2.VideoCapture(0)

#Defining facemesh using mediapipe
facemesh = mp.solutions.face_mesh.FaceMesh()

while True:

    #Activate webcam
    _, frame = cam.read()

    #Convert BGR frame to RGB frame using opencv
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = facemesh.process(rgbframe)

    #Obtaining landmarks
    landmarkpoints = output.multi_face_landmarks
    frameheight, framewidth, _ = frame.shape


    if landmarkpoints:

        landmarks = landmarkpoints[0].landmark

        for landmark in landmarks:
            #x,y coordinates corresponding to centre of face
            x = int(landmark.x * framewidth)
            y = int(landmark.y * frameheight)

            #Drawing circles corresponding to landmarks using opencv
            cv2.circle(frame, (x,y), 3, (0, 255, 0))

    cv2.imshow('Face detection', frame)
    cv2.waitKey(1)