class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = sum(candies) // k
        while(left < right):
            mid = (left + right + 1) // 2
            cnt = 0
            for candy in candies:
                cnt += candy // mid
            if cnt < k:
                right = mid - 1
            else:
                left = mid
        return right