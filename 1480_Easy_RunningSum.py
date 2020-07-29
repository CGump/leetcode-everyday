# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 1480_Easy_RunningSum.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/7/29 16:04
#
# ================================================================


class Solution:

    def runningSum(self, nums: list) -> list:
        temp = [nums[0]]
        for i in range(1, len(nums)):
            result = nums[i] + temp[i-1]
            temp.append(result)
        return temp