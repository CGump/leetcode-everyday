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
    
    def isValid_leetcode(self, s):
        """
        官方解法
        栈 + 字典搜索
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # 如果char 存在于字典mapping中，这里检索的是字典的key。
            # 也就是说，如果是右括号，则要进行比较
            if char in mapping:

                # 当char在mapping的key里，这时候要和栈顶的元素进行配对
                # 如果栈是空的，给定一个'#'字符串作为对比标志
                # 其实栈是空的，那么说明这个右括号一定是 孤立 的
                top_element = stack.pop() if stack else '#'

                # 此时按key的值与栈顶元素进行比较
                # 不匹配，则返回False
                if mapping[char] != top_element:
                    return False
            else:
                # 如果char是左括号，就先推入栈中
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        # 最后，如果栈是空的，则返回True（not stack = true）
        return not stack

if __name__ == "__main__":
    rst = Solution()
    ans = rst.isValid(")[[[()]]]")
    print(ans)