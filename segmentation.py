# -*- coding: utf-8 -*-
import maximumMatching
from preprocessingSentence import sentenceProcessing
from conditionalProbabilityEvaluate import bestCasesEvaluate
from dictionaryRead import *
from maximumMatching import maximumMatchingGraph
"""Use azetteer dictionary to sentence segmentation for each sentence do the segmentation"""


def segmentation(sentenceList):
    """ segment a bunch of sentences """
    dictionary = readTrainSetDictionary()
    dictionary.sort(key=len, reverse=True)
    signdict = readSignDictionary()
    # foreigns = readGeographyDictionary()
    foreigns=[]
    segments = []
    for sentence in sentenceList:
        segment=[]
        atomSegmented = sentenceProcessing(sentence,signdict)
        for phrase in atomSegmented:
            if len(phrase.split(' '))>1:
                maximumMatchingCases = maximumMatchingGraph(phrase, dictionary)
                segment+=maximumMatchingCases
            else:
                segment.append(phrase)
        segments.append(segment)
    return segments