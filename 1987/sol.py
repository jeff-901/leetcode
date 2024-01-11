class Solution(object):
    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        zero_flag = "0" in binary
        idx = 0
        while(idx < len(binary) and binary[idx] == "0"):
            idx += 1
        s = 0
        dp = [0, 0]
        while(idx < len(binary)):
            if binary[idx] == "1":
                added = s + 1 - dp[1]
                dp[1] = s + 1
                s += added
            else:
                added = s - dp[0]
                dp[0] = s
                s += added
            idx += 1
        if zero_flag:
            s += 1
        return s % (10**9 + 7)