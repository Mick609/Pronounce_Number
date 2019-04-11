#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:20:05 2019

@author: mick
"""
import os
from gtts import gTTS
import pygame

def get_name(argument):
    names = {
        0: "",
        1: "Thousand",
        2: "Million",
        3: "Billion",
        4: "Trillion",
        5: "Quadrillion",
        6: "Billion",
        7: "Quintillion",
        8: "Sextillion",
        9: "Septillion"
    }
    return names.get(argument, "Invalid get_name")
def get_eng_digit(number):
    num = str(number)
    digits = {
        '1': "One",
        '2': "Twe",
        '3': "Three",
        '4': "Four",
        '5': "Five",
        '6': "Six",
        '7': "Seven",
        '8': "Eight",
        '9': "Nine"
    }
    return digits.get(num, "Invalid get_eng_digit")
def pronounce_num_smaller_than_hundred(number):
    tys = {
        '2': "Twenty",
        '3': "Thirty",
        '4': "Forty",
        '5': "Fifty",
        '6': "Sixty",
        '7': "Seventy",
        '8': "Eighty",
        '9': "Ninty"}
    teens =  {
        '11': "Eleven",
        '12': "Twelve",
        '13': "Thirteen",
        '14': "Fourteen",
        '15': "Fifteen",
        '16': "Sixteen",
        '17': "Seventeen",
        '18': "Eighteen",
        '19': "Ninteen"}
    num = str(number)
    opt = ''
    if len(num) == 2:
        if num[0] == '1':
            opt = teens.get(num, "Invalid pronounce_num_smaller_than_hundred")
        else:
            opt = tys.get(num[0], "Invalid pronounce_num_smaller_than_hundred") + ' ' + get_eng_digit(num[1])
    elif len(num) == 1:
        opt = get_eng_digit(num)
    else:
        print('Error: Number bigger than limit.')
        opt = '-1'
    return opt
def pronounce_num_smaller_than_thousand(number):
    num = str(number)
    opt = ''
    if len(num) == 3:
        dummy = num[1] + num[2]
        opt = get_eng_digit(num[0]) + ' Hundred and ' + pronounce_num_smaller_than_hundred(dummy)
        
    elif len(num) < 3:
        opt = pronounce_num_smaller_than_hundred(num)
    return opt

def pronounce(number):
    num = str(number)
    opt = ''
    if len(num) <= 3:
        opt = (pronounce_num_smaller_than_thousand(num))
    else:
        numbers_per_thousand = []
        dummy_num_str = ''
        for i in range(len(num)):
            index = len(num) - i - 1
            if len(dummy_num_str) == 3:
                numbers_per_thousand.append(dummy_num_str)
                dummy_num_str = ''
                dummy_num_str = num[index]
            else:
                dummy_num_str = num[index] + dummy_num_str
            
        numbers_per_thousand.append(dummy_num_str)
        for i in range(len(numbers_per_thousand)):
            index = len(numbers_per_thousand) - i - 1
            opt = opt + (pronounce_num_smaller_than_thousand(numbers_per_thousand[index]) + ' ' + get_name(index)) + ' '
    tts = gTTS(text=opt, lang='en')
    tts.save("num.mp3")
    pygame.init()
    pygame.mixer.music.load('num.mp3')
    pygame.mixer.music.play()
    return opt, tts


if __name__ == '__main__':
    text, tts = (pronounce(123456123124123123124123789))