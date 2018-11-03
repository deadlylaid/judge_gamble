#!/usr/bin/pythons
#-*-coding:utf-8-*-

import cv2
import numpy as np
import pytesseract as py

class ExtractTargetText(object):
    """
    Input: 이미지 디렉토리 경로 / ex) '/home/taemin/site_images/edited_real.png'
    Output: 타겟 단어(현재 베팅내역) 에 대한 화면의 픽셀 포인트 값
    * 단일 코드 테스트를 위해서는 현재와 같이 주석처리를 하고 실행, 코드 통합시에는 주석처리 반대로
    """
    # def __init__(self, image_path_):
    def __init__(self):
    #     self.raw_image = cv2.imread(image_path_)
        # 이미지 받아오기
        self.raw_image = cv2.imread('/home/taemin/site_images/edited_real.png')
        self.target_point_x = 0
        self.target_point_y = 0

    def extract_text(self):
        # 이미지 그레이 스케일로 변환
        gray_image = cv2.cvtColor(self.raw_image, cv2.COLOR_BGR2GRAY)
        # 이미지 블러 처리(노이즈 제거를 위한 뭉뚝하게)
        blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        # 일정 임계치 이상(60)의 포인트들은 일정값(255)로 처리됨
        _, threshed_image = cv2.threshold(gray_image, 60, 255, cv2.THRESH_BINARY_INV)
        # 윤곽선 추출 / 글자영역을 잘 추출하기 위해서는 임계점 설정과 더불러 다른 전처리 과정들이 필요함. 구글링.
        _, contours, hierachy = cv2.findContours(threshed_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 윤곽선 추출로 생성된 영역들
        rects = [cv2.boundingRect(each) for each in contours]
        print(rects)
        # 일정 크기의 영역들만 계산함.
        filtered_rects = [(x, y, w, h) for (x, y, w, h) in rects if ((w * h > 10) and (w * h < 1000000))]
        print(filtered_rects)
        image_number = 1
        for rect in filtered_rects:
            # Draw the rectangles
            margin = 0
            cv2.rectangle(self.raw_image, ((rect[0] - margin), (rect[1] - margin)), ((rect[0] + rect[2] + margin), (rect[1] + rect[3] + margin)), (0, 255, 0), 5)
            # 해당 영역을 잘라내고 크기 확대 / 글자 인식을 향상시키기 위해서지만 효과가 없는듯 함.
            cropped_image = gray_image[(rect[1] - margin): (rect[1] + rect[3] + margin),
                            (rect[0] - margin): (rect[0] + rect[2] + margin)]
            height, width = cropped_image.shape[:2]
            resized_cropped_image = cv2.resize(cropped_image, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
            # 해당 영역의 이미지에서의 글자 인식
            text = py.image_to_string(resized_cropped_image, lang='kor', config='-psm 7 -c preserve_interword_spaces=1')
            print(text)
            # ㄴ"베팅내역" 판별시에 위치정보
            point_x = rect[0] + (rect[2] / 2)
            point_y = rect[1] + (rect[3] / 2)
            if text.encode('utf-8') == "베팅내역":
                self.target_point_x = point_x
                self.target_point_y = point_y
                position_of_target = (point_x, point_y)
                # print(text)
                # print("position = ", position_of_target)
                margin2 = 10
                # cv2.rectangle(self.raw_image, ((rect[0] - margin2), (rect[1] - margin2)),
                #               ((rect[0] + rect[2] + margin2), (rect[1] + rect[3] + margin2)), (255, 255, 0), 5)
            # print(text)
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(raw_image, text.encode('utf-8'), (point_x, point_y), font, 2, (0, 0, 255), 2)
            # image_name = "image_" + str(image_number) + ".jpg"
            # cv2.imwrite(image_name, cropped_image)
            # image_number += 1
        # resized_image = cv2.resize(threshed_image, (1920, 1080))
        # cv2.imshow("test", resized_image)
        # cv2.waitKey(0)
        return self.target_point_x, self.target_point_y

if __name__ == '__main__':
    test = ExtractTargetText()
    test.extract_text()

