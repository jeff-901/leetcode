class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """
        left = 0
        right = k
        while(left <= right):
            mid = (left + right) // 2
            tmp = mid
            cnt = 0
            while(tmp > 0):
                cnt += tmp
                tmp //= 5
            if cnt > k:
                right = mid - 1
            elif cnt == k:
                return 5
            else:
                left = mid + 1
        return 0