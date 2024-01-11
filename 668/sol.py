class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        left = 1
        right = m * n
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            for i in range(1, m+1):
                cnt += min(mid // i, n)
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        return left