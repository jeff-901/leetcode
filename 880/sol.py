class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = 0
        idx = 0
        for i, ele in enumerate(s):
            if ele.isdigit():
                l *= int(ele)
            else:
                l += 1
            if l >= k:
                idx = i
                break
        while(k < l or s[i].isdigit()):
            if s[i].isdigit():
                l = l / int(s[i])
                k = (k-1) % l + 1
            else:
                l -= 1
            i -= 1
        return s[i]