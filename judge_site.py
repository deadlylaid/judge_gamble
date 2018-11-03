#!/usr/bin/pythons3
#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup
import re
from konlpy import jvm
from konlpy.tag import Twitter
import numpy as np
import pandas as pd

class JudgeSite():

    def __init__(self):
        print('Start Web Crawling')
        print('Road the site list')
        # 트레이닝 데이터 오간
        self.training_data = []
        # 사이트 리스트를 받을 변수
        self.dobaac_urls = []
        self.normal_urls = []
        # 파일 불러오기
        dobaac_file = open('/home/taemin/site_list/bad_site.txt')
        while True:
            line = dobaac_file.readline()
            line = line.rstrip('\n')
            if not line: break
            self.dobaac_urls.append(line)
        print(self.dobaac_urls)
        normal_file = open('/home/taemin/site_list/good_site.txt')
        while True:
            line = normal_file.readline()
            line = line.rstrip('\n')
            if not line: break
            self.normal_urls.append(line)
        print(self.normal_urls)

    def crawling(self, url):
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        # html tag 제거
        cleaned_text = re.sub('[a-zA-Z]', '', str(soup))
        cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', cleaned_text)
        # 한글 추출
        except_hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
        hangul = except_hangul.sub('', cleaned_text)
        return hangul

    def collect_training_data(self):
        # 리스트 구조 [Number, Sentences, Label]
        whole_data = []
        # 도박사이트 정보 받아오기
        for i in range(len(self.dobaac_urls)):
            print("{} 번째 도박사이트 웹정보를 받아오고 있습니다.".format(i+1))
            words = np.array(" ".join(self.crawling(self.dobaac_urls[i]).split()))
            label = np.ones(1)
            data = np.hstack([words, label])
            data = np.hstack([i+1, data])
            whole_data.append(data)
        print("도박사이트의 웹정보를 받아왔습니다.")
        # 일반사이트 정보 받아오기
        for i in range(len(self.normal_urls)):
            print("{} 번째 일반사이트 웹정보를 받아오고 있습니다.".format(i+1))
            words = np.array(" ".join(self.crawling(self.dobaac_urls[i]).split()))
            label = np.zeros(1)
            data = np.hstack([words, label])
            data = np.hstack([i+1, data])
            whole_data.append(data)
        print("일반사이트의 웹정보를 받아왔습니다.")
        self.training_data = np.array(whole_data)
        print(self.training_data)

    def word2vec(self):
        # pass
        # 명사 추출
        spliter = Twitter()
        print("에러가 날 것이다.")
        # nouns = spliter.nouns(hangul)
    #     # 중복된 명사 제거
    #     deduplicated_nouns = list(set(nouns))
    #     result = deduplicated_nouns
    #     return result


if __name__ == '__main__':
    jvm.init_jvm()
    judge_site = JudgeSite()
    judge_site.collect_training_data()
    judge_site.word2vec()