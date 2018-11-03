#!/usr/bin/pythons
#-*-coding:utf-8-*-

import cv2
import pytesseract as py
import re
import numpy as np

class ExtractText(object):
    """

    """
    def __init__(self, image_path_):
        self.raw_image = cv2.imread(image_path_)

    def preprocess_image(self):
        gray_image = cv2.cvtColor(self.raw_image, cv2.COLOR_BGR2GRAY)
        blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        _, threshed_image = cv2.threshold(blur_image, 100, 255, cv2.THRESH_BINARY_INV)
        contours, hierachy = cv2.findContours(threshed_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        whole_text = py.image_to_string(threshed_image, lang='kor', config='-psm 3 -c preserve_interword_spaces=1')
        cleaned_text = re.sub('[a-zA-Z]', '', whole_text)
        cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
        for x in cleaned_text.split():
            if len(x.encode('ascii', 'ignore')) == 5:
                password = x.encode('ascii', 'ignore')
                print(password)
        # print([len(x.encode('ascii', 'ignore')) for x in cleaned_text.split()])
        # rects = [cv2.boundingRect(each) for each in contours]
        # print(rects)
        # filtered_rects = [(x, y, w, h) for (x, y, w, h) in rects if ((w * h > 1000) and (w * h < 10000))]
        # for rect in rects:
        #     # Draw the rectangles
        #     margin = 0
        #     cv2.rectangle(self.raw_image, ((rect[0] - margin), (rect[1] - margin)), ((rect[0] + rect[2] + margin), (rect[1] + rect[3] + margin)), (0, 255, 0), 5)
        #     cropped_image = gray_image[(rect[1] - margin): (rect[1] + rect[3] + margin),
        #                     (rect[0] - margin): (rect[0] + rect[2] + margin)]
        #     height, width = cropped_image.shape[:2]
        #     resized_cropped_image = cv2.resize(cropped_image, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
        #     text = py.image_to_string(resized_cropped_image, lang='kor', config='-psm 7 -c preserve_interword_spaces=1')
        #     # "베팅내역" 판별시에 위치정보
        #     point_x = rect[0] + (rect[2] / 2)
        #     point_y = rect[1] + (rect[3] / 2)
        #     # if text.encode('utf-8') == "베팅내역":
        #     #     position_of_target = (point_x, point_y)
        #     #     print(text)
        #     #     print("position = ", position_of_target)
        #     #     margin2 = 10
        #     #     cv2.rectangle(self.raw_image, ((rect[0] - margin2), (rect[1] - margin2)),
        #     #                   ((rect[0] + rect[2] + margin2), (rect[1] + rect[3] + margin2)), (255, 255, 0), 5)
        #     # print(text)
        #     # font = cv2.FONT_HERSHEY_SIMPLEX
        #     # cv2.putText(raw_image, text.encode('utf-8'), (point_x, point_y), font, 2, (0, 0, 255), 2)
        #     # image_name = "image_" + str(image_number) + ".jpg"
        #     # cv2.imwrite(image_name, cropped_image)
        # resized_image = cv2.resize(self.raw_image, (1920, 1080))
        # cv2.imshow("test", resized_image)
        # cv2.waitKey(0)

# raw_image = cv2.imread()

if __name__ == '__main__':
    image_path = "/home/taemin/site_images/login.png"
    extracter_text = ExtractText(image_path)
    extracter_text.preprocess_image()