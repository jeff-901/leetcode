class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        n = len(customers)
        grumpy_times = collections.deque()
        ans = 0
        grumpy_sum = 0
        max_sum = 0
        for i in range(n):
            if grumpy[i] == 1:
                grumpy_sum += customers[i]
                grumpy_times.append(i)
                while(grumpy_times and grumpy_times[0] <= i - minutes):
                    grumpy_sum -= customers[grumpy_times.popleft()]
                max_sum = max(max_sum, grumpy_sum)
            else:
                ans += customers[i]
        while(grumpy_times and grumpy_times[0] < n - minutes):
            grumpy_sum -= customers[grumpy_times.popleft()]
        max_sum = max(max_sum, grumpy_sum)
        
        return ans + max_sum