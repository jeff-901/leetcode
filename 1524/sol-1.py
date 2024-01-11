class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        odd = 0
        even = 0
        for num in arr:
            even += 1
            if num % 2:
                even, odd = odd, even
            ans += odd
        return ans % (10**9+7)