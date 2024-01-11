class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """ 
        if len(s) < 2:
            return ""
        elements = set(s)
        res = ""
        res_l = 0
        start = 0
        for i in range(len(s)):
            if s[i].swapcase() not in elements:
                if i - start > res_l:
                    tmp = self.longestNiceSubstring(s[start:i])
                    if len(tmp) > res_l:
                        res = tmp
                        res_l = len(tmp)
                start = i + 1
        if start == 0:
            return s
        if len(s) - start > res_l:
            tmp = self.longestNiceSubstring(s[start:])
            if len(tmp) > res_l:
                res = tmp
        return res
                
        
        