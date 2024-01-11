class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = [False for _ in range(n+1)]
        for i in range(n):
            if ans[i] == False:
                cnt = 1
                while(i + cnt ** 2 <= n):
                    ans[i+cnt**2] = True
                    cnt += 1
        return ans[-1]