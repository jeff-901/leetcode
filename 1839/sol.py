class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        cur = 0
        ans = 0
        cnt = 0
        h = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        for c in word:
            if h[c] == cur:
                cnt += 1
            elif h[c] == cur + 1 and cnt > 0:
                cur += 1
                cnt += 1
            else:
                if cur == 4:
                    ans = max(ans, cnt)
                cur = 0
                if h[c] == 0:
                    cnt = 1
                else:
                    cnt = 0
        if cur == 4:
            ans = max(ans, cnt)
        return ans