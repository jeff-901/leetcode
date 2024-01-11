class Solution(object):
    def getLengthOfOptimalCompression(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        h = {}
        def dp(idx, last_chr, cnt, k):
            if k < 0:
                return float("inf")
            if idx >= n:
                return 0
            if (idx, last_chr, cnt, k) in h:
                return h[(idx, last_chr, cnt, k)]
            ans = 0
            incr = 0
            if s[idx] == last_chr:
                if cnt == 1 or cnt == 9 or cnt == 99:
                    incr = 1
                ans = incr + dp(idx+1, last_chr, cnt+1, k)
            else:
                ans = min(1 + dp(idx+1, s[idx], 1, k), dp(idx+1, last_chr, cnt, k-1))
            h[(idx, last_chr, cnt, k)] = ans
            return ans
        return dp(0, None, 0, k)