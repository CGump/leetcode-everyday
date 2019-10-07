class Solution:
    '''
    编写一个函数来查找字符串数组中的最长公共前缀。   
    如果不存在公共前缀，返回空字符串 ""。   

    示例 1:   
    输入: ["flower","flow","flight"]   
    输出: "fl"

    示例 2:   
    输入: ["dog","racecar","car"]   
    输出: ""   
    解释: 输入不存在公共前缀。 

    说明:   
    所有输入只包含小写字母 a-z 。
    '''
    def longestCommonPrefix(self, strs) -> str:
        if strs == []:
            return ""
        word = strs[0]
        i = 0
        ans = ""
        for item in word:
            for code in strs:
                if len(code) <= i or code[i] != item:
                    return ans
            ans += item
            i += 1
        return ans
    
    def longestCommonPrefix1(self, strs):
        '''
        这里应用了解压的方法，通过zip(*)将字符串数组纵向解压成
        元组列表（会自动忽略多余的，不对齐的项）
        如：['flower', 'flash', 'flow'] 会分解成
        [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'a', 'o'), ('w', 's', 'w')]
        然后用set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据。
        当set函数结果大于1时说明重复的项不止1个，此时输出上一次的所有项即可。
        '''
        s = ""
        for i in zip(*strs):
            if len(set(i))==1:
                s += i[0]
            else:
                break           
        return s  

if __name__ == "__main__":
    rst = Solution()
    ans = rst.longestCommonPrefix(["flower","flow","flight"])
    print(ans)