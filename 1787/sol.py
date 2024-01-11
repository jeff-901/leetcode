class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        if k == 1:
            for ele in nums:
                if ele != 0:
                    ans+=1
            return ans

        count = [{} for _ in range(k)]
        for i, ele in enumerate(nums):
            count[i%k][ele] = count[i%k].get(ele, 0) + 1
        n = len(nums)
        dp = [[0 for _ in range(1024)] for _ in range(k)]
        for ele in count[0]:
            dp[0][ele] = count[0][ele]
        last = max(dp[0])
        for i in range(1, k):
            for num in range(1024):
                dp[i][num] = last
                for ele in count[i]:
                    dp[i][num] = max(dp[i][num], dp[i-1][num^ele] + count[i][ele])
            last = max(dp[i])
        return n - dp[-1][0]