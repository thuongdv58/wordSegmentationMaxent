# # -*- coding: utf-8 -*-
from segmentation import segmentation
import sys

def test():
    if len(sys.argv) == 3:
        print 'shit'
    else:
        segments= segmentation(['Thể chất và trí tuệ còn rất non nớt mà sớm bị "cài đặt game" online vào trí não (có chiến thuật, có tranh đua, có thu phí) thì sẽ có nhiều tác hại về lâu về dài, phụ huynh này nói và bày tỏ mong muốn Bộ Giáo dục'])
        for segment in segments:
            print u'**'.join([token.decode('utf-8') for token in segment])
if __name__ == "__main__":
    # print sys.argv
    test()
# import argparse

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print args.accumulate(args.integers)