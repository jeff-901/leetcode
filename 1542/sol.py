class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = {0: -1}
        total = 0
        ans = 0
        for i in range(len(s)):
            total ^= 1 << int(s[i])
            for j in range(10):
                ans = max(ans, i - cnt.get(total ^ (1 << j), i))
            if total in cnt:
                ans = max(ans, i - cnt[total])
            else:
                cnt[total] = i
        return ans
        
            