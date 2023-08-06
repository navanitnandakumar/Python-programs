#Importing required modules
import cv2
import mediapipe as mp
import pyautogui as pg

#Define cam as webcam
cam = cv2.VideoCapture(0)

#Defining facemesh with refined landmarks
facemesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)

#Obtaining screen width and screen height
screenw, screenh = pg.size()

#Infinite loop
while True:

    #Read webcam
    _, frame = cam.read()

    #Flipping frame
    frame = cv2.flip(frame, 1)

    #Convert BGR frame to RGB frame using opencv
    rgbframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = facemesh.process(rgbframe)

    #Obtaining landmarks
    landmarkpoints = output.multi_face_landmarks

    #Obtaining frameheight & framewidth
    frameh, framew, _ = frame.shape


    if landmarkpoints:

        #Required landmarks
        landmarks = landmarkpoints[0].landmark

        #Choosing right eye for movement
        #Detecting right eye
        #landmarks[474:478] denotes right eye landmarks

        #id stores index, landmark stores element
        for id, landmark in enumerate(landmarks[474:478]):

            #x,y coordinates corresponding to centre of face
            x = int(landmark.x * framew)
            y = int(landmark.y * frameh)

            #Drawing circle corresponding to landmark
            cv2.circle(frame, (x, y), 3, (255, 0, 0))

            #Moving mouse as eye moves
            #Choosing a particular landmark on the eye
            if id == 1:

                #Scaling x & y accordingly to cover entire screen
                screenx = (screenw / framew) * x
                screeny = (screenh / frameh) * y

                #moving cursor to scaled coordinates
                pg.moveTo(screenx, screeny)

        #Choosing left eye for clicking
        #Detecting left eye
        lefteye = [landmarks[145], landmarks[159]]

        for landmark in lefteye:

            #x,y coordinates corresponding to centre of face
            x = int(landmark.x * framew)
            y = int(landmark.y * frameh)

            #Drawing circle corresponding to landmark
            cv2.circle(frame, (x, y), 3, (0, 0, 255))

        #Detecting upper eyelid of left eye
        upeyelid = lefteye[0].y

        #Detecting lower eyelid of left eye
        loweyelid = lefteye[1].y

        #detecting blink
        if((upeyelid - loweyelid) < 0.01):

            #If blink is detected, activate mouse click
            pg.click()
            pg.sleep(1)

    #Show reults
    cv2.imshow('Eye controlled mouse', frame)
    cv2.waitKey(1)