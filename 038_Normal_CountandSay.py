# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 038_Normal_CountandSay.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/6/30 14:49
#
# ================================================================


class Solution:
    """
    给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
    注意：整数序列中的每一项将表示为一个字符串。
    「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    第一项是数字 1
    描述前一项，这个数是 1 即 “一个 1 ”，记作 11
    描述前一项，这个数是 11 即 “两个 1 ” ，记作 21
    描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211
    描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221
    """
    def countAndSay(self, n: int) -> str:
        ans = '1'
        while n != 1:
            num = []
            note = []
            m = 0
            for i in range(0, len(ans)):
                if num == [] and note == []:
                    num.append(ans[i])
                    note.append(1)
                    continue
                if ans[i] == ans[i-1]:
                    note[m] += 1
                else:
                    num.append(ans[i])
                    note.append(1)
                    m += 1
            ans = ''
            for i in range(0, len(num)):
                ans = ans + str(note[i]) + str(num[i])
            n -= 1
        return ans