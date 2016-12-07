# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import xml.etree.ElementTree as ET
import glob
import csv
import codecs
reload(sys)
sys.setdefaultencoding('utf8')

""" read dictionary from xml_form or csv_form 
which is converted from xml_form for faster speed""" 

def readXMLNormalWordDictionary():
    wordList = [u'a']
    fileList = glob.glob('dictionary/normal_word_dictionary/*.xml')
    for file in fileList:
        dictionaryTree = ET.parse(file)
        root = dictionaryTree.getroot()
        for entry in root.iter('Entry'):
            word = entry[0].text
            if type(word) != type(u'a'):
                word = word+u''
            if word != wordList[-1]:
                wordList.append(word)
    return wordList

def readGeographyDictionary():
    """ geographic place dictionary sumarized from NGA GEOnet Names Server """
    data=codecs.open('dictionary/Geographic_dictionary', 'r', 'utf-8').read()
    return data.split('\n')

def readCsvNormalWordDictionary():
    content = codecs.open('dictionary/dictionary.csv', 'r', 'utf-8').read()
    return content.split(',')


def readTrainSetDictionary():
    content = codecs.open('dictionary/trainingSetDict', 'r', 'utf-8').read()
    return content.split('\n')
    
def readSignDictionary():
    content = codecs.open('dictionary/signDictionary', 'r', 'utf-8').read()
    return content.split('\n')

# dictionary= readXMLdictionary()
# content= u','.join(dictionary)
# file= open('dictionary/dictionary.csv','w').write(content)