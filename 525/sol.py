class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {0:-1}
        balance = 0
        ans = 0
        for i, num in enumerate(nums):
            balance += 1 if num else -1
            if balance in h:
                ans = max(ans, i-h[balance])
            else:
                h[balance] = i
        return ans