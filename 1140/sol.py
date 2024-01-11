class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        h = {}
        n = len(piles)
        for i in range(n-1, 0, -1):
            piles[i-1] += piles[i]
        def f(start, m):
            if start + m * 2 >= n:
                return piles[start]
            if start > n - 1:
                return 0
            if (start, m) in h:
                return h[(start, m)]
            opponent = float("inf")
            for i in range(1, m+1):
                opponent = min(opponent, f(start+i, m))
            for i in range(m+1, 2*m+1):
                opponent = min(opponent, f(start+i, i))
            h[(start, m)] = piles[start] - opponent
            return h[(start, m)]
        return f(0, 1)