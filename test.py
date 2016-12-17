# # -*- coding: utf-8 -*-
from segmentation import segmentation
import sys

def test():
    segments= segmentation(['Thằng Hoàng sdsf fasdfsad adsfasd ăn'])
    for segment in segments:
        print u'**'.join([token.decode('utf-8') for token in segment])
if __name__ == "__main__":
    test()