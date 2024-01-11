class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mydict = {'0':0, '1':1, '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9} 
        mod = 10**9 + 7
        dp = [0]*(len(s)+1)
        dp[-1] = 1
        for i in range (len(s)-1,-1,-1):
            if s[i] != '0':
                cur = 0
                index = i
                while index < len(s) and cur <= k:
                    cur*=10
                    cur+=mydict[s[index]]
                    if cur <= k:
                        dp[i]+=dp[index+1]%mod
                    index+=1
        return dp[0]%mod