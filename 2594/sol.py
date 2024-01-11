class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        n = len(ranks)
        left = min(ranks)
        right = (((cars + n - 1) // n) ** 2) * max(ranks)
        h = {}
        for r in ranks:
            h[r] = h.get(r, 0) + 1
        while(left <= right):
            mid = (left + right) // 2
            s = 0
            for r in h:
                s += h[r] * math.floor(math.sqrt(mid // r))
            if s < cars:
                left = mid + 1
            else:
                right = mid - 1
        return left