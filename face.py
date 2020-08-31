#

import cv2


# load pre trained data

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#choose an image to detect face
"""
img = cv2.imread('NAR.png')
"""
webcam = cv2.VideoCapture(0)


while True:

    sucess_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img,scaleFactor=1.5,minNeighbors=5)
     

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h) , (0,255,0),10)
    cv2.imshow('unqcoder',frame)
    stop=cv2.waitKey(1)

    if stop==49:
        break


#make photo in gray scale
#grayscaled_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#decete faces
#face_coordinates=trained_face_data.detectMultiScale(grayscaled_img,scaleFactor=1.5,minNeighbors=5)
#rectangle around the face
#(x,y,w,h)=face_coordinates[0]

#for (x,y,w,h) in face_coordinates:
#cv2.rectangle(img,(x,y),(x+w,y+h) , (0,255,0),10)

#cv2.imshow('unqcoder',img)
 
#cv2.waitKey()
