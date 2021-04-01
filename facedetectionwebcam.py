import cv2

#load the cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Give the input
cap = cv2.VideoCapture(0)

#Set the size of the window
cap.set(3,640)
cap.set(4,480)
#Set the brightness
cap.set(10,150)

while True:
    succuss,img = cap.read()
    #convert the colored image to gray 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #Detect the face
    faces = faceCascade.detectMultiScale(gray, 1.3, 4)
    #Draw rectangle around the faces
    for (x, y, w, h) in faces :
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #Show the output
    cv2.imshow("result", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
