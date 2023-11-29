import cv2

human_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cats_cascade = cv2.CascadeClassifier('cat.xml')
dog_cascade =cv2.CascadeClassifier("mydogdetector.xml")

img = cv2.imread('./image/sample2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

humans = human_cascade.detectMultiScale(gray, 1.3, 4) # detect human face

for (x, y, w, h) in humans:
    #print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cats = cats_cascade.detectMultiScale(gray, scaleFactor=1.78, minNeighbors=3, minSize=(45, 45)) # detect cat face

for (x, y, w, h) in cats:
    #print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

dogs = dog_cascade.detectMultiScale(gray, 1.91, 3) # detect dog face

for (x, y, w, h) in dogs:
    #print(x, y, w, h)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cattext = f"Total cats : {len(cats)}"
humantext = f"Total humans : {len(humans)}"
dogtext = f"Total dogs : {len(dogs)}"


sum = 30

if len(humans) != 0:
    image = cv2.putText(img, humantext, (0, sum), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2) # print total humans
    if sum == 30:
        sum = 60
    elif sum == 60:
        sum = 90
    

if len(cats) != 0:
    image = cv2.putText(img, cattext, (0, sum), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2) # print total cats
    if sum == 30:
        sum = 60
    elif sum == 60:
        sum = 90
    

if len(dogs) != 0:
    image = cv2.putText(img, dogtext, (0, sum), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2) # print total dogs
    if sum == 30:
        sum = 60
    elif sum == 60:
        sum = 90
    

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()