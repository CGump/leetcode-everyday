# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 069_Normal_SqrtX.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/7/3 15:59
#
# ================================================================


class Solution:
    """
    实现 int sqrt(int x) 函数。
    计算并返回 x 的平方根，其中 x 是非负整数。
    由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

    示例 1:
    输入: 4
    输出: 2

    示例 2:
    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842...,
         由于返回类型是整数，小数部分将被舍去。
    """
    def mySqrt(self, x: int) -> int:
        """
        对于任意整数，有a^2 <= x <= (a+1)^2，通过这个进行二分查找，快速找到目标值
        :param x:
        :return:
        """
        left = 0
        right = x + 1  # 这个+1很tm关键！！！！！！！！！！！！！！！！！！！
        while True:
            p = (left + right) // 2
            if p ** 2 <= x < (p + 1) ** 2:
                return p
            else:
                if p ** 2 > x:
                    right = p
                else:
                    left = p

    def my_sqrt(self, x):
        """
        公式转换法，sqrt(x)= x^(1/2) = (e^(ln x))^(1/2) = e^(0.5*ln x)
        :param x:
        :return:
        """
        import math
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans  # 这里要判断ans和ans+1哪个比目标值更小

