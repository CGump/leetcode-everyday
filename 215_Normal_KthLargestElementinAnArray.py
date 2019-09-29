class Solution:
    """
    在未排序的数组中找到第 k 个最大的元素。   
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    示例 1:   
    输入: [3,2,1,5,6,4] 和 k = 2   
    输出: 5

    示例 2:    
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4   
    输出: 4
    """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #nums_new = []
        #for temp in nums:
        #    if temp not in nums_new:
        #        nums_new.append(temp)
        #    else:
        #        pass
        #以上可以剔除相同元素
        nums.sort(reverse=True)
        return nums[k-1]

if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    rst = Solution()
    print(rst.findKthLargest(nums, k))