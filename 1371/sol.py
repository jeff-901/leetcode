class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vis = 0
        vowel = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        h = {0: -1}
        ans = 0
        for i, ch in enumerate(s):
            if ch in vowel:
                vis ^= 1 << vowel[ch]
                if vis in h:
                    ans = max(ans, i - h[vis])
                else:
                    h[vis] = i
            else:
                ans = max(ans, i - h[vis])
        return ans