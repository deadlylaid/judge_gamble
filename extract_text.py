#!/usr/bin/pythons
#-*-coding:utf-8-*-

import cv2
import numpy as np
import pytesseract as py

# raw_image = cv2.imread("/home/taemin/site_images/test_number.jpeg")
raw_image = cv2.imread("/home/taemin/site_images/real.png")
gray_image = cv2.cvtColor(raw_image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
_, threshed_image = cv2.threshold(blur_image, 50, 300, cv2.THRESH_BINARY_INV)
contours, hierachy = cv2.findContours(threshed_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rects = [cv2.boundingRect(each) for each in contours]
filtered_rects = [(x, y, w, h) for (x, y, w, h) in rects if ((w * h > 10) and (w * h < 1000000))]
image_number = 1
for rect in filtered_rects:
    # Draw the rectangles
    margin = 0
    # cv2.rectangle(raw_image, ((rect[0] - margin), (rect[1] - margin)), ((rect[0] + rect[2] + margin), (rect[1] + rect[3] + margin)), (0, 255, 0), 5)
    cropped_image = gray_image[(rect[1] - margin) : (rect[1] + rect[3] + margin), (rect[0] - margin) : (rect[0] + rect[2] + margin)]
    height, width = cropped_image.shape[:2]
    resized_cropped_image = cv2.resize(cropped_image, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
    text = py.image_to_string(resized_cropped_image, lang='kor', config='-psm 7 -c preserve_interword_spaces=1')
    # "베팅내역" 판별시에 위치정보
    point_x = rect[0] + (rect[2] / 2)
    point_y = rect[1] + (rect[3] / 2)
    if text.encode('utf-8') == "베팅내역":
        position_of_target = (point_x, point_y)
        print(text)
        print("position = ", position_of_target)
        margin2 = 10
        cv2.rectangle(raw_image, ((rect[0] - margin2), (rect[1] - margin2)), ((rect[0] + rect[2] + margin2), (rect[1] + rect[3] + margin2)), (255, 255, 0), 5)
    # print(text)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(raw_image, text.encode('utf-8'), (point_x, point_y), font, 2, (0, 0, 255), 2)
    image_name = "image_" + str(image_number) + ".jpg"
    cv2.imwrite(image_name, cropped_image)
    image_number += 1
resized_image = cv2.resize(raw_image, (1920, 1080))
cv2.imshow("test", resized_image)
cv2.waitKey(0)