# # -*- coding: utf-8 -*-
from segmentation import segmentation
import sys

def test():
	if len(sys.argv) == 3:
		print 'shit'
	else:
		print segmentation(['Quan hệ tình dục sớm , mang thai ngoài ý muốn'])

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