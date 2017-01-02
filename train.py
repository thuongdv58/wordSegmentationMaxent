# -*- coding: utf-8 -*-
# encoding=utf8

import sys
reload(sys)
sys.path.append('/')
sys.setdefaultencoding('utf8')
import xml.etree.ElementTree as ET
import glob
import csv
import codecs
import json
import io
from dateutil.parser import parse
from preprocessingSentence import *
from dictionaryRead import *


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
    wordDictionary = {1: [], 2: [], 3: [], 4: [], 5: []}
    signDict = readSignDictionary()
    sentenceList = csvTrainingFile()
    for sentence in sentenceList:
        wordlist = sentence.split(' ')
        for index in range(len(wordlist)):
            word = wordlist[index]
            syllables = word.split('_')
            joinedWord = ' '.join(syllables)
            if index == 0:
                # if re.match("^[A-Z]",wordlist[0]) and re.match("^[a-z]",wordlist[1]):
                #     wordlist[0]= wordlist[0][0].lower()+wordlist[0][1:]
                if len(syllables) == 1:
                    if syllables[0] == '' or syllables[0] == ' ' or vietnameseDecimalMatch(word) or dateFormatMatch(word) or URLFormatMatch(word) or word in signDict:
                        continue
                    add = Lower(syllables[0][0])+syllables[0][1:]
                    if add not in wordDictionary[1]:
                        wordDictionary[1].append(add)
                    continue
                if isUpper(syllables[0][0]):
                    if isLower(syllables[1][0]):
                        syllables[0] = Lower(syllables[0][0])+syllables[0][1:]
                        if ' '.join(syllables) not in wordDictionary[min(len(syllables), 5)]:
                            wordDictionary[min(len(syllables), 5)].append(
                                ' '.join(syllables))
                    else:
                        if not joinedWord in wordDictionary[min(len(syllables), 5)]:
                            wordDictionary[
                                min(len(syllables), 5)].append(joinedWord)
            else:
                if not vietnameseDecimalMatch(word) and not dateFormatMatch(word) and not URLFormatMatch(word) and word not in signDict:
                    if not joinedWord in wordDictionary[min(len(syllables), 5)]:
                        wordDictionary[
                            min(len(syllables), 5)].append(joinedWord)

    return wordDictionary


def bigramTrain():

    bigramCount = {}
    unigramCount = {}
    wordCount = 0
    sentenceList = csvTrainingFile()
    for sentence in sentenceList:
        wordlist = sentence.split(' ')
        wordCount += len(wordlist)
        wordlist = ['</s>']+wordlist
        for index in range(1,len(wordlist)):
            word=wordlist[index]
            preWord=wordlist[index-1]
            if unigramCount.has_key(word):
                unigramCount[word] += 1
            else:
                unigramCount[word] = 1

            if bigramCount.has_key(word):
                if bigramCount[word].has_key(preWord):
                    bigramCount[word][preWord]+=1
                else:
                    bigramCount[word][preWord]=1
            else:
                bigramCount[word] = {}
                bigramCount[word][preWord]=1
    return bigramCount, unigramCount, wordCount
def readUnigram():
    return json.load(open("trainedModel/unigramCount.csv",'r'))
def readBigram():
    return json.load(open('trainedModel/bigramCount.csv','r'))
def readWordCount():
    data= codecs.open('trainedModel/wordCount.csv', 'r', 'utf-8').read()
    return int(data)
def linearInterpolationTrain():
    alpha1=0.981
    alpha2=0.019
    return alpha1,alpha2
# dictionary= createNewDictionaryFile() 
# file= open('dictionary/trainingSetDictionary.csv','w').write(u'\n'.join(dictionary))
# dicts=createNewDictionaryFile() print dicts[1] dicts[1].sort()
# dicts[2].sort() dicts[3].sort() dicts[4].sort() dicts[5].sort()
# file=open('dictionary/oneWordDict.csv','w').write(u'\n'.join(dicts[1])) 
# file=open('dictionary/twoWordDict.csv','w').write(u'\n'.join(dicts[2])) 
# file=open('dictionary/threeWordDict.csv','w').write(u'\n'.join(dicts[3])) 
# file=open('dictionary/fourWordDict.csv','w').write(u'\n'.join(dicts[4])) 
# file=open('dictionary/fiveWordDict.csv','w').write(u'\n'.join(dicts[5]))

# bi, uni, count = bigramTrain()
# with io.open('trainedModel/bigramCount.csv','w',encoding='utf8') as jsonFile:
#     data = json.dumps(bi, ensure_ascii=False, encoding='utf8')
#     jsonFile.write(unicode(data))
# with io.open('trainedModel/unigramCount.csv','w',encoding='utf8') as jsonFile:
#     data = json.dumps(uni, ensure_ascii=False, encoding='utf8')
#     jsonFile.write(unicode(data))
# file =open('trainedModel/wordCount.csv','w').write(str(count))

# d2 = json.load(open("text.txt"))
