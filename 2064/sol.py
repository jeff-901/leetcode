class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        left = 1
        right = max(quantities)
        while(left <= right):
            mid = (left + right) // 2
            cnt = 0
            for q in quantities:
                cnt += (q + mid - 1) // mid
            # print(mid, cnt)
            if cnt > n:
                left = mid + 1
            else:
                right = mid - 1
        return left