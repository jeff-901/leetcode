class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        price.sort()
        left = 0
        right = (price[-1] - price[0] + k - 2) // (k - 1)
        while(left <= right):
            mid = (left + right) // 2
            cnt = 1
            cur = price[0]
            for p in price:
                if p - cur >= mid:
                    cnt += 1
                    cur = p
            if cnt < k:
                right = mid - 1
            else:
                left = mid + 1
        return right