class Solution(object):
    def findIntegers(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return n + 1
        bits = len(bin(n)) - 2
        dp = [0] * (bits) 
        dp[0] = 2
        dp[1] = 3
        for i in range(2, bits):
            dp[i] = dp[i-1] + dp[i-2]
        def find(n):
            if n < 3:
                return n + 1
            bits = len(bin(n)) - 2
            left = n - 2 ** (bits-1)
            if left >= 2**(bits-2):
                return dp[bits-1]
            else:
                return dp[bits-2] + find(left)
        return find(n)