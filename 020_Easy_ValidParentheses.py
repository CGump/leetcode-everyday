class Solution:
    '''
    给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串，判断字符串是否有效。   
    有效字符串需满足：   
        左括号必须用相同类型的右括号闭合。   
        左括号必须以正确的顺序闭合。   
    注意空字符串可被认为是有效字符串。

    示例 1:   
    输入: "()"   
    输出: true   

    示例 2:   
    输入: "()[]{}"   
    输出: true   

    示例 3:   
    输入: "(]"   
    输出: false   

    示例 4:   
    输入: "([)]"   
    输出: false

    示例 5:   
    输入: "{[]}"   
    输出: true
    '''
    def isValid(self, s: str) -> bool:
        S = []
        dict_s = {')':'(', ']':'[', '}':'{'}
        for item in s:
            if item == '(' or item == '[' or item == '{':
                S.append(item)
            elif S ==[]:
                S.append(item)
            elif dict_s[item] == S[-1]:
                S.pop()
            else:
                S.append(item)
        return True if S == [] else False

if __name__ == "__main__":
    rst = Solution()
    ans = rst.isValid(")[[[()]]]")
    print(ans)