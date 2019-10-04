class Solution:
    '''
    罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
    
    字符          数值
    I             1   
    V             5   
    X             10   
    L             50   
    C             100   
    D             500   
    M             1000   

    例如， 罗马数字 2 写做 II ，即为两个并列的 1。   
    12 写做 XII ，即为 X + II 。   
    27 写做  XXVII, 即为 XX + V + II 。

    通常情况下，罗马数字中小的数字在大的数字的右边。   
    但也存在特例，例如 `4` 不写做 `IIII`，而是 `IV`。   
    数字 `1` 在数字 `5` 的左边，所表示的数等于大数 `5` 减小数 `1` 得到的数值 `4` 。   
    同样地，数字 `9` 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

    给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
    '''
    def romanToInt(self, s: str) -> int:
        '''
        思路解析：
        给定一串罗马数字 `MMCMLXIV'
        当C在M左边时，表示为900。以此规律可以看出：
        如果当前位比下一位大或者相等时，正常累加当前位的数值；
        如果当前位比下一位小时，则当前位应执行减去的操作；
        如：
        M记为1000，MM记为1000+1000，
        MMC时，下一位为M，则此时C记为1000+1000-100
        MMCM时，记为1000+1000-100+1000
        即可正常显示罗马字母的
        '''
        num = {'I':1, 'V':5, 'X':10, 'L':50,
              'C':100, 'D':500, 'M':1000}
        sum_roma = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                sum_roma += num[s[i]]
                break
            elif num[s[i]] >= num[s[i+1]]:
                sum_roma += num[s[i]]
            else:
                sum_roma -= num[s[i]]
        return sum_roma

if __name__ == "__main__":
    rst = Solution()
    ans = rst.romanToInt('MMCMLXIV')
    print(ans)