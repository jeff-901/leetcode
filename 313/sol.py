class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        cands = [(p, p, 1) for p in primes]
        heapq.heapify(cands)
        ugly_num = [1]

        for _ in range(n - 1):
            ugly_num.append(cands[0][0])
            while cands[0][0] == ugly_num[-1]:
                x, p, i = heapq.heappop(cands)
                heapq.heappush(cands, (p*ugly_num[i], p, i + 1))
        return ugly_num[-1]