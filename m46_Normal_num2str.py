class Solution:
    """
    给定一个数字，我们按照如下规则把它翻译为字符串：
    0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
    一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

    输入: 12258   
    输出: 5   
    解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

    """

    def translateNum(self, num: int) -> int:
        string = str(num)
        length = len(string)

        def find(pointer):
            if pointer >= length - 1:
                return 1
            temp = string[pointer:pointer + 2]
            if '10' <= temp <= '25':
                return find(pointer + 1) + find(pointer + 2)
            else:
                return find(pointer + 1)

        return find(0)


if __name__ == "__main__":
    rst = Solution()
    print(rst.translateNum(18580))
