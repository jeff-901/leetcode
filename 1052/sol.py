class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        ans = 0
        grumpy_sum = 0
        max_sum = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                grumpy_sum += customers[i]
            else:
                ans += customers[i]
        max_sum = max(max_sum, grumpy_sum)
        for i in range(minutes, n):
            if grumpy[i-minutes] == 1:
                grumpy_sum -= customers[i-minutes]
            if grumpy[i] == 1:
                grumpy_sum += customers[i]
                max_sum = max(max_sum, grumpy_sum)
            else:
                ans += customers[i]
        if grumpy[n-minutes] == 1:
                grumpy_sum -= customers[n-minutes]
        max_sum = max(max_sum, grumpy_sum)
        
        return ans + max_sum