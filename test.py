# # -*- coding: utf-8 -*-
from segmentation import segmentation
import sys

def test():
    segments= segmentation(['Ô thể chất và trí tuệ còn rất non nớt mà sớm bị "cài đặt','Thân áo rộng, quần thụng cạp cao, dép quai hậu... là phong cách đặc trưng của người Bắc trước thời kỳ Đổi mới, trong khi miền Nam đa phong cách hơn.','2-3 4-6, 5/6/2016 ggdkm ds8hdsi'])
    for segment in segments:
        print u'**'.join([token.decode('utf-8') for token in segment])
if __name__ == "__main__":
    test()