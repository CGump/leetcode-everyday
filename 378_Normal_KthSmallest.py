# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 378_Normal_KthSmallest.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/7/2 11:08
#
# ================================================================


class Solution:
    """
    给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
    请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

    示例：
    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ],
    k = 8,
    返回 13。
    """
    def kthSmallest(self, matrix: list, k: int) -> int:
        new = []
        for item in matrix:
            new += item
        new.sort()
        return new[k-1]
