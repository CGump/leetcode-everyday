# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 003_Normal_LongestSubstring.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/6/16 9:15
#
# ================================================================


class Solution:
    """
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

    示例 1:
    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

    示例 2:
    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

    示例 3:
    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max_len = 0  # 最大窗口距离
        note = 0  # 当前窗口的大小
        old = []  # 当前窗口内的值
        left = 0  # 记录窗口划过的位置
        for item in s:
            note += 1
            while item in old:
                old.remove(s[left])
                left += 1
                note -= 1
            if note > max_len:
                max_len = note
            old.append(item)

        return max_len


if __name__ == '__main__':
    s = 'dvdf'
    rst = Solution().lengthOfLongestSubstring(s)
    print(rst)
