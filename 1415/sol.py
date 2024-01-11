class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ""
        ch = ["a", "b", "c"]
        if 3 * (2 ** (n-1)) < k:
            return ""
        k -= 1
        ans += ch[k // (2**(n-1))]
        k %= 2**(n-1)
        n -= 1
        while(n > 0):
            idx = k // 2**(n-1)
            k %= 2**(n-1)
            cnt = 0
            while(cnt <= idx):
                if ans[-1] == ch[cnt]:
                    idx += 1
                cnt += 1
            ans += ch[cnt - 1]
            n -= 1
        return ans