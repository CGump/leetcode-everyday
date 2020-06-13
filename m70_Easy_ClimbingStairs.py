# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : m70_Easy_ClimbingStairs.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/6/13 8:39
#
# ================================================================


class Solution:
    """
    假设你正在爬楼梯。需要n阶你才能到达楼顶。
    每次你可以爬1或2个台阶。
    你有多少种不同的方法可以爬到楼顶呢？
    注意：给定n是一个正整数。

    实例1：
    输入： 3
    输出： 3
    解释： 有三种方法可以爬到楼顶。
    1.  1 阶 + 1 阶 + 1 阶
    2.  1 阶 + 2 阶
    3.  2 阶 + 1 阶
    """

    def climbStairs(self, n: int) -> int:
        """
        斐波那契数列
        :param n:
        :return:
        """

        def cb(n):
            if n == 1 or n == 0:
                return 1
            else:
                return cb(n - 1) + cb(n - 2)

        return cb(n)

    def climbStairs_1(self, n, use):
        """
        记忆化递归
        :param n:输入阶梯数
        :param use: 已计算过的值
        :return:
        """
        use = {0: 1, 1: 1}

        def cb(n, use):
            if n in use.keys():
                return use[n]
            else:
                rst = cb(n - 1, use) + cb(n - 2, use)
                use[n] = rst
                return use[n]

        return cb(n, use)


if __name__ == '__main__':
    pass
