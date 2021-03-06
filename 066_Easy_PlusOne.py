class Solution(object):
    '''
    给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。   
    最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。   
    你可以假设除了整数 0 之外，这个整数不会以零开头。   
    
    示例 1:   
    输入: [1,2,3]   
    输出: [1,2,4]   
    解释: 输入数组表示数字 123。

    示例 2:   
    输入: [8,9,9,9]   
    输出: [9,0,0,0]   
    解释: 输入数组表示数字 8999。
    '''
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) - 1
        while l >= 0:
            if digits[l] < 9:
                digits[l] += 1
                break
            else:
                digits[l] = 0
                l -= 1 
        if digits[0] == 0:
            return [1] + digits
        else:
            return digits

if __name__ == "__main__":
    rst = Solution()
    ans = rst.plusOne([8, 9, 9, 9])
    print(ans)