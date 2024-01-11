class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        zero = 0
        one = 0
        zero_one = 0
        one_zero = 0
        for i in range(len(s)):
            if s[i] == "1":
                one += 1
                zero_one += zero
                ans += one_zero
            else:
                zero += 1
                one_zero += one
                ans += zero_one
        return ans