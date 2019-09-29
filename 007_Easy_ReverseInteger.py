class Solution:
    '''
    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

    示例 1:   
    输入: 123   
    输出: 321

    示例 2:   
    输入: -123   
    输出: -321
    '''
    def reverse(self, x: int) -> int:
        num = str(x)[::-1].rstrip('-')
        
        if int(num) < 2**31:
            if x >= 0:
                return int(num)
            else:
                return 0 - int(num)
        return 0