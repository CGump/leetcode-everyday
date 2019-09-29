class Solution:
    '''
    一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。   
    作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。   
    当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。   
    给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。   
    其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。   
    接下来会给出一组访问次数和域名组合的列表cpdomains。   
    要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。   

    示例 1:   
    输入:    
    ["9001 discuss.leetcode.com"]   
    输出:    
    ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]    
    说明:    
    例子中仅包含一个网站域名："discuss.leetcode.com"。按照前文假设，子域名"leetcode.com"和"com"都会被访问，所以它们都被访问了9001次。
    '''
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dicts = {} #字典
        for item in cpdomains:
            array = item.split(' ') #split分割字符串
            num = (int)(array[0])
            domain = array[1]
            domainLen = len(domain.split('.'))
            for i in range(domainLen):
                tmp = domain.split('.',i).pop()
                if tmp in dicts.keys():
                    dicts[tmp]=dicts[tmp]+num
                else:
                    dicts[tmp]=num
        domainList=[]
        for key in dicts:
            tmp = (str)(dicts[key])+" "+key
            domainList.append(tmp) # 在domainlist结尾添加tmp
        return domainList

if __name__ == "__main__":
    rst = Solution()
    testCpdomains = ["9001 discuss.leetcode.com"]
    print(rst.subdomainVisits(testCpdomains))
    testCpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(rst.subdomainVisits(testCpdomains))
    