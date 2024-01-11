class Solution(object):
    def countHousePlacements(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, second = 1, 2
        for i in range(1, n):
            tmp = first
            first = second
            second = (first + tmp) % 1000000007
        return second * second % 1000000007