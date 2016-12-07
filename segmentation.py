# -*- coding: utf-8 -*-
import maximumMatching
from preprocessingSentence import sentenceAtomSegmentation
from conditionalProbabilityEvaluate import bestCasesEvaluate
from dictionaryRead import *
from maximumMatching import maximumMatchingSegment
"""Use azetteer dictionary to sentence segmentation for each sentence do the segmentation"""


def segmentation(sentenceList):
    """ segment a bunch of sentences """
    dictionary = readTrainSetDictionary()
    signdict = readSignDictionary()
    foreigns = readGeographyDictionary()
    segments = []
    for sentence in sentenceList:
        atomSegmented = sentenceAtomSegmentation(sentence)
        maximumMatchingCases = maximumMatchingSegment(
            atomSegmented, dictionary, signdict, foreigns, 4)
        segments.append(bestCasesEvaluate(maximumMatchingCases))
    return segments


def main():
    """ for test only """
    dictionary = readTrainSetDictionary()
    signdict = readSignDictionary()
    foreigns = readGeographyDictionary()
    segments = maximumMatchingSegment(sentenceAtomSegmentation(
        "Quan hệ tình dục sớm , mang thai ngoài ý muốn , nhiễm các bệnh lây lan qua đường tình dục , nạo phá thai tràn lan , đặc biệt là ở lứa tuổi vị thành niên đã trở thành mối lo chung của toàn xã hội ."), dictionary, signdict, foreigns, 4)
    for segment in segments:
        print u'**'.join([token.decode('utf-8') for token in segment])

if __name__ == "__main__":
    main()
