#!/usr/bin/pythons
#-*-coding:utf-8-*-

import extract_text2

test_instance = extract_text2.ExtractText('/home/taemin/site_images/login.png')
print(test_instance.preprocess_image())
