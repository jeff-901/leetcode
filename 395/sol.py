class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def isSubStr(s,k):
            if len(s) < k:
                return 0
            h={}
            for i, ele in enumerate(s):
                if ele in h:
                    h[ele]+=1
                else:
                    h[ele]=1
            end = 0
            start = 0
            ans = 0
            while(end < len(s)):
                if h[s[end]] < k:
                    ans = max(ans, isSubStr(s[start:end], k))
                    start = i+1
                end += 1
            if start == 0:
                return len(s)
            if start < len(s):
                ans = max(ans, isSubStr(s[start:], k))     
            return ans
        return isSubStr(s,k)