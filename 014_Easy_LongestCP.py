# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 014_Easy_LongestCP.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/6/15 16:16
#
# ================================================================


class Solution:
    """
    编写一个函数来查找字符串数组中的最长公共前缀。
    如果不存在公共前缀，返回空字符串""。

    示例
    输入: ["flower", "flow", "flight"]
    输出: "fl"
    """
    def longestCommonPrefix(self, strs) -> str:
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for item in ss:
            item = list(item)
            if len(item) > 1:
                break
            res = res + item[0]

        return res


if __name__ == '__main__':
    ans = Solution()
    rst = ans.longestCommonPrefix(["flower", "flow", "flight"])
    print(rst)
