import cv2

#'haarcascade_frontalface_default.xml' needs to be downloaded before running
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#capturing video using webcam
#for detecting faces in a video, add file path in VideoCapture()
cap = cv2.VideoCapture(0)

#infinite loop for generating frames from the video
while True:
    _, image = cap.read()
    #convert to grayscale before running
    grayscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayscale, 1.1, 4)

    #creating rectangular boundary over face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)

    #to display result
    cv2.imshow('image', image)

    #press 'esc' to exit
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
