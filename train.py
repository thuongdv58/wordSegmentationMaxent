# -*- coding: utf-8 -*-
# encoding=utf8

import sys
import xml.etree.ElementTree as ET
import glob
import csv
import codecs
from dateutil.parser import parse
reload(sys)
sys.setdefaultencoding('utf8')
import preprocessingSentence


def readTrainningData():
    globalSentenceList = []
    fileList = glob.glob('trainingDataSet/segmentedSet/*.seg')
    for file in fileList:
        data = codecs.open(file, 'r', 'utf-8').read()
        sentenceList = data.split('\n')
        sentenceList = filter(
            lambda sentence: sentence != '' and sentence[0] != '<', sentenceList)
        globalSentenceList += sentenceList[1:]
    file = open('trainingDataSet/trainingData.csv',
                'w').write(u'\n'.join(globalSentenceList))
    return globalSentenceList


def csvTrainingFile():
    data = codecs.open('trainingDataSet/trainingData.csv', 'r', 'utf-8').read()
    return data.split('\n')


def createNewDictionaryFile():
    wordDictionary = []
    sentenceList = csvTrainingFile()
    for sentence in sentenceList:
        wordlist = sentence.split(' ')
        for word in wordlist:
            if not vietnameseDecimalMatch(word) and not dateFormatMatch(word) and not word in wordDictionary:
                wordDictionary.append(word)
    return wordDictionary

# dictionary= createNewDictionaryFile()
# file= open('dictionary/trainingSetDictionary.csv','w').write(u'\n'.join(dictionary))
