# # -*- coding: utf-8 -*-
from segmentation import segmentation
import sys
import codecs
def test():
    segments= segmentation(['Thằng Hoàng sdsf fasdfsad adsfasd ăn','dsfjsdj sdfsdifjhi'])
    for segment in segments:
    	try:
    		print '**'.join([token.encode('utf-8') for token in segment])
    	except Exception:
    		print '**'.join([token for token in segment])
if __name__ == "__main__":
    test()