class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            s = 0
            for w in weights:
                if s + w > mid:
                    cnt += 1
                    s = w
                else:
                    s += w
            cnt += 1
            if cnt <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left