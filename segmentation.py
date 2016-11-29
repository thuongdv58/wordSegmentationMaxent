# -*- coding: utf-8 -*-
import maximumMatching
import preprocessingSentence
# import conditionalProbabilityEvaluate
from dictionaryRead import readCsvNormalWordDictionary
from maximumMatching import maximumMatchingSegment
"""Use azetteer dictionary to sentence segmentationfor each sentencedo the segmentation"""

def main():
    dictionary = readCsvNormalWordDictionary()
    segments = maximumMatchingSegment(
        "một con chó tè vào con mèo", dictionary, 4)
    segments = maximumMatchingSegment(
        "bưu điện gần thành phố hà nội", dictionary, 4)
    segments = maximumMatchingSegment(
        "người dùng trong mảng kinh doanh hàng đầu thế giới", dictionary, 4)
    for segment in segments:
        print u'//'.join([token.decode('utf-8') for token in segment])

if __name__ == "__main__":
	main()