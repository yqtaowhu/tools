#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2020-02-13 19:56:54 


from utils.langconv import Converter #

def cat_to_chs(sentence): #传入参数为列表
        """
        将繁体转换成简体
        :param line:
        :return:
        """
        sentence =",".join(sentence)
        sentence = Converter('zh-hans').convert(sentence)
        sentence.encode('utf-8')
        return sentence.split(",")


def chs_to_cht(sentence):#传入参数为列表
        """
        将简体转换成繁体
        :param sentence:
        :return:
        """
        sentence =",".join(sentence)
        sentence = Converter('zh-hant').convert(sentence)
        sentence.encode('utf-8')
        return sentence.split(",")

def Traditional2Simplified(sentence):
    '''
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    '''
    sentence = Converter('zh-hans').convert(sentence)
    return sentence

def Simplified2Traditional(sentence):
    '''
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    '''
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


if __name__ == '__main__':
    sentence = "黄鹤楼"
    convert_sen = Simplified2Traditional(sentence)
    print(convert_sen)

    sentence_1 = "北京大學"
    convert_sen_1 = Traditional2Simplified(sentence_1)
    print(convert_sen_1)
    