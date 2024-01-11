class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def calSteps(cur):
            cnt = 0
            level = 0
            while(cur + 10**level - 1 <= n):
                cnt += 10**level
                cur *= 10
                level += 1
            if n - cur + 1 > 0:
                cnt += n - cur + 1
            return cnt

        cur = 1
        k = k - 1
        while (k > 0):
            steps = calSteps(cur)
            if (steps <= k):
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur
