class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        vis = set()
        if 2**k+(k-1) > len(s):
            return False
        num = 0
        for i in range(k-1):
            num <<= 1
            if s[i] == "1":
                num += 1
        bit_mask = 2 ** k - 1
        for i in range(k-1, len(s)):
            num = (num << 1) & bit_mask
            if s[i] == "1":
                num += 1
            vis.add(num)
        if len(vis) == 2 ** k:
            return True
        else:
            return False