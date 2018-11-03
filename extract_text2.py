#!/usr/bin/pythons
#-*-coding:utf-8-*-

import cv2
import pytesseract as py
import re

class ExtractText(object):
    """

    """
    def __init__(self, image_path_):
        self.raw_image = cv2.imread(image_path_)

    def preprocess_image(self):
        gray_image = cv2.cvtColor(self.raw_image, cv2.COLOR_BGR2GRAY)
        blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        _, threshed_image = cv2.threshold(blur_image, 100, 255, cv2.THRESH_BINARY_INV)
        whole_text = py.image_to_string(threshed_image, lang='kor', config='-psm 3 -c preserve_interword_spaces=1')
        cleaned_text = re.sub('[a-zA-Z]', '', whole_text)
        cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
        for x in cleaned_text.split():
            if len(x.encode('ascii', 'ignore')) == 5:
                password = x.encode('ascii', 'ignore')
                return password