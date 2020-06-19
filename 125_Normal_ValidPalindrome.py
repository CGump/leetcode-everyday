# -*- coding: utf-8 -*-
# ================================================================
#
#   Editor      : PyCharm
#   File name   : 125_Normal_ValidPalindrome.py
#   Author      : CGump
#   Email       : huangzhigang93@gmail.com
#   Created date: 2020/6/19 10:18
#
# ================================================================


class Solution:
    """
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    说明：本题中，我们将空字符串定义为无效的回文串。

    示例 1:
    输入: "A man, a plan, a canal: Panama"
    输出: true

    示例 2:
    输入: "race a car"
    输出: false
    """
    def isPalindrome(self, s: str) -> bool:
        """
        通过ASCII码表位置进行过滤，然后反序对比是否一致
        :param s:
        :return:
        """
        new_s = ""
        for item in s:
            if 48 <= ord(item) <= 57 or 65 <= ord(item) <= 90 or 97 <= ord(item) <= 122:
                new_s = new_s + item
        new_s = new_s.lower()
        print(new_s)
        if new_s == new_s[::-1]:
            return True
        else:
            return False

    def isPalindrome2(self, s: str) -> bool:
        """
        通过双指针的方式对前后进行索引比较
        :param s:
        :return:
        """
        new_s = "".join(ch.lower() for ch in s if ch.isalnum())
        length = len(new_s)
        print(new_s)
        for i in range(0, length):
            if new_s[i] != new_s[length-i-1]:
                return False
            if i >= (length - i):
                return True


    def isPalindrome3(self, s: str) -> bool:
        """
        直接在源字符串上比较
        :param s:
        :return:
        """
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True


if __name__ == '__main__':
    ans = Solution()
    rst = ans.isPalindrome2('A man, a plan, a canal: Panama')
    print(rst)