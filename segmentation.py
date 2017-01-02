# -*- coding: utf-8 -*-
import maximumMatching
from preprocessingSentence import sentenceProcessing
from conditionalProbabilityEvaluate import bestCasesEvaluate
from dictionaryRead import *
from maximumMatching import maximumMatchingGraph
"""Use azetteer dictionary to sentence segmentation for each sentence do the segmentation"""
from train import readBigram,readUnigram,readWordCount,linearInterpolationTrain
from conditionalProbabilityEvaluate import phraseLinearInterpolationChoose
def segmentation(sentenceList):
    """ segment a bunch of sentences """
    dictionary = readWordCountDictionary()
    signdict = readSignDictionary()
    # foreigns = readGeographyDictionary()
    alpha1,alpha2= linearInterpolationTrain()
    foreigns=[]
    segments = []
    for sentence in sentenceList:
        segment=[]
        atomSegmented = sentenceProcessing(sentence,signdict)
        for phrase in atomSegmented:
            if len(phrase.split(' '))>1:
                maximumMatchingCases = maximumMatchingGraph(phrase, dictionary)
                segment+=maximumMatchingCases
                # segment+=phraseLinearInterpolationChoose(maximumMatchingCases,readUnigram(),readBigram(),readWordCount(),alpha1,alpha2)
            else:
                segment.append(phrase)
        segments.append(segment)
    return segments

if __name__ == "__main__":
    filename = raw_input("input filename to segment> ")
    data = codecs.open(filename, 'r', 'utf-8').read()
    sentences= data.split('\n')

segments= segmentation(sentences)
for segment in segments:
    print u' '.join(['_'.join(token.decode('utf-8').split(' ')) for token in segment])