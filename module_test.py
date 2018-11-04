#!/usr/bin/pythons
#-*-coding:utf-8-*-

import extract_text2

test_instance = extract_text2.ExtractText('login.png')
print(test_instance.preprocess_image())
