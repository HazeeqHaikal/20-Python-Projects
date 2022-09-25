import cv2

faceCascade = cv2.CascadeClassifier("default.xml")

img = cv2.imread("./image/cr7.png")

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(grey, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)  

cv2.imwrite("./image/face_detected.jpg", img)