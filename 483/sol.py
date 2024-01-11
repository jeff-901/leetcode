class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)
        ans = n
        left = 2
        right = n
        for bit in range(1, int(math.log(n+1, 2) + 1)):
            left = 2
            while(left <= right):
                mid = (left + right) // 2
                diff = (mid ** bit) - 1 - n * (mid - 1)
                if diff > 0:
                    right = mid - 1
                elif diff < 0:
                    left = mid + 1
                else:
                    ans = min(ans, mid)
                    break
        return str(ans)