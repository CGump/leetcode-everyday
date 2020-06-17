# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 1014_Normal_BestSightseeingPair.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/6/17 11:48
#
# ================================================================


class Solution:
    """
    给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
    一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
    返回一对观光景点能取得的最高分。

    示例：
    输入：[8,1,5,2,6]
    输出：11
    解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
    """

    def maxScoreSightseeingPair(self, A: list) -> int:
        rst = 0
        length = len(A)
        ai_max = A[0] + 0
        for j in range(1, length):
            rst = max(rst, ai_max + A[j] - j)
            ai_max = max(ai_max, A[j] + j)
        return rst


if __name__ == "__main__":
    ans = Solution()
    result = ans.maxScoreSightseeingPair([8, 1, 5, 2, 6])
    print(result)
