class Solution:
    '''
    给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。   
    说明：每次只能向下或者向右移动一步。   

    示例:   
    输入:   
    [[1,3,1],   
     [1,5,1],   
     [4,2,1]]   
    输出: 7   
    解释: 因为路径 1→3→1→1→1 的总和最小。   
    '''
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sums = list(grid[0])
        for j in range(1, len(grid[0])):
            sums[j] = sums[j - 1] + grid[0][j]
        for i in range(1, len(grid)):
            sums[0] += grid[i][0]
            for j in range(1,len(grid[0])):
                sums[j] = min(sums[j - 1], sums[j]) + grid[i][j]
        return sums[-1]
    
if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    rst = Solution()
    ans = rst.minPathSum(grid)
    print(ans)