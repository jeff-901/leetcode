class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t2 = 0
        t3 = 0
        t5 = 0
        n -= 1
        ans = [1]
        while(n > 0):
            ans.append(min(ans[t2] * 2, ans[t3] * 3, ans[t5] * 5))
            if ans[-1] == ans[t2] * 2:
                t2 += 1
            if ans[-1] == ans[t3] * 3:
                t3 += 1
            if ans[-1] == ans[t5] * 5:
                t5 += 1
            n -= 1
        # print(ans)
        return ans[-1]