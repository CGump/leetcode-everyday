# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 1431_Easy_Kids.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/6/13 17:07
#
# ================================================================


class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        """
        给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。
        对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，
        此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有#最多#的糖果数目.

        示例 1：
        输入：candies = [2,3,5,1,3], extraCandies = 3
        输出：[true,true,true,false,true]
        解释：
        孩子 1 有 2 个糖果，如果他得到所有额外的糖果（3个），那么他总共有 5 个糖果，他将成为拥有最多糖果的孩子。
        孩子 2 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
        孩子 3 有 5 个糖果，他已经是拥有最多糖果的孩子。
        孩子 4 有 1 个糖果，即使他得到所有额外的糖果，他也只有 4 个糖果，无法成为拥有糖果最多的孩子。
        孩子 5 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
        :param candies:
        :param extraCandies:
        :return:
        """
        def maximum(candies):
            maxs = candies[0]
            for i in range(1, len(candies)):
                if candies[i] > maxs:
                    maxs = candies[i]
            return maxs
        max_num = maximum(candies)
        rst = []
        for item in candies:
            if (item + extraCandies) >= max_num:
                rst.append(True)
            else:
                rst.append(False)
        return rst


if __name__ == '__main__':
    ans = Solution()
    result = ans.kidsWithCandies(candies=[2,3,5,1,3], extraCandies=3)
    print(result)