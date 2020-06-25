# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 139_Normal_WordBreak.py
#   Author      : CGump
#   Email       : huangzhigang93@qq.com
#   Created date: 2020/6/25 19:05
#
# ================================================================


class Solution:
    """
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
    判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
    说明：
    拆分时可以重复使用字典中的单词。
    你可以假设字典中没有重复的单词。

    示例 1：
    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true
    解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

    示例 2：
    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
         注意你可以重复使用字典中的单词。

    示例 3：
    输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出: false
    """
    def wordBreak(self, s: str, wordDict: list) -> bool:
        if not wordDict:
            return False

        flags = [0]
        for i in range(0, len(s) + 1):
            for j in flags:
                if s[j:i] in wordDict:
                    flags.append(i)
                    break

        return flags[-1] == len(s)


"""
解题思路

以"catsdog"，["cats","dog","cat"]进行举例，
思路是如果前i个子字符串存在于字典中，
那么只需要比较后len(s)-i个是否在字典当中，
并同时记录下此时前i个字符串的长度。

注意一点的是，
当判断到cat在字典中时，
此时flags=[0,3]，
进行下一个循环时i=4，
字串会分别选取s[0:4]和s[3:4],
此时s[0:4]="cats"也出现在字典中，
于是被记录下来并跳出内循环。
这点是精髓之处。

"""