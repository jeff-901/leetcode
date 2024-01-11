class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        dp = []
        previous_smaller_idx = 0
        for idx, num in enumerate(arr):
            while(stack and arr[stack[-1]] > num):
                stack.pop()    
            if not stack:
                dp.append(num * (idx + 1))
            else:
                previous_smaller_idx = stack[-1]
                dp.append(dp[previous_smaller_idx] + (idx-previous_smaller_idx) * num)
            stack.append(idx)
        return sum(dp) % (10**9 + 7)
