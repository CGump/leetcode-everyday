class Solution:
    '''
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

    示例 1:   
    输入: s = "anagram", t = "nagaram"   
    输出: true   

    示例 2:   
    输入: s = "rat", t = "car"   
    输出: false
    '''
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        new_s = sorted(list(s))
        new_t = sorted(list(t))
        lenS = len(new_s)
        lenT = len(new_t)
        if lenS != lenT:
            return False
        else:
            if new_s == new_t:
                return True
            else:
                return False
if __name__ == "__main__":
    rst = Solution()
    print(rst.isAnagram('anagram', 'nagaram'))
    print(rst.isAnagram('rat', 'car'))