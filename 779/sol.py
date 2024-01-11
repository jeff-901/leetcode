class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ans = 0
        k -= 1
        for i in range(n):
            ans ^= k % 2
            k //= 2
        return ans
