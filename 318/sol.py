class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        h = {}
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - 97)
            h[mask] = max(h.get(mask, 0), len(word))
        ans = 0
        for x in h:
            for y in h:
                if x & y == 0:
                    ans = max(ans, h[x] * h[y])
        return ans
