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
            i = 1
            j = n
            while(i <= m):
                while(j > 0 and j * i > mid):
                    j -= 1
                cnt += j
                i += 1
            if cnt < k:
                left = mid + 1
            else:
                right = mid - 1
        return left