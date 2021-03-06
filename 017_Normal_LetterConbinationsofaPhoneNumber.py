class Solution:
    '''
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。   
    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

    示例:   
    输入："23"   
    输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

    说明:   
    尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
    '''
    def letterCombinations(self, digits: str):
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        if digits == "":
            return []
        ans = ['']
        for num in digits:
            ans = [item+word for item in ans for word in phone[num]]
        return ans
    
    def letterCombinations1(self, digits: str):
        '''
        该函数自定义一个迭代数组实现上述功能
        使用3个for循环
        和一个额外空间backfun
        ''' 
        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        if digits == "":
            return []
        ans = ['']
        for num in digits:
            backfun = []
            for item in ans:
                for word in phone[num]:
                    backfun.append(item + word)
            ans = backfun
        return ans

if __name__ == "__main__":
    rst = Solution()
    ans = rst.letterCombinations(digits='')
    print(ans)
    ans = rst.letterCombinations(digits='23')
    print(ans)
