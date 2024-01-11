class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if m*k > n:
            return -1
        left = 1
        right = max(bloomDay)
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            adjacent = 0
            for i in range(n):
                if bloomDay[i] <= mid:
                    adjacent += 1
                    if adjacent >= k:
                        adjacent -= k
                        cnt += 1
                        if cnt >= m:
                            break
                else:
                    adjacent = 0
            if cnt < m:
                left = mid + 1
            else:
                right = mid - 1
        return left