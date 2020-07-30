# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 1512_Easy_NumberofGoodPairs.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/7/30 15:47
#
# ================================================================
class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        count = 0
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count