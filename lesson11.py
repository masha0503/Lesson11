import cv2
from PIL import Image

image_path = 'img/people.jpg'
image_people = cv2.imread(image_path)

people_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
people_face = people_face_cascade.detectMultiScale(image_people)

people = Image.open('img/people.jpg')
robot = Image.open('img/robot.png')

people = people.convert('RGBA')
robot = robot.convert('RGBA')

for (x, y, w, h) in people_face:
    cv2.rectangle(image_people, (x, y), (x + w, y + h), (0, 128, 0), 2)

cv2.imshow('image_people', image_people)
cv2.waitKey(3000)

for (x, y, w, h) in people_face:
    robot = robot.resize((w, h))
    people.paste(robot, (x, y), robot)

people.save('people_robot.png')

people_robot = cv2.imread('people_robot.png')

cv2.imshow('people_robot', people_robot)
cv2.waitKey()