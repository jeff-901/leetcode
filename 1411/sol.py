class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        two_color = 6
        three_color = 6
        for _ in range(1, n):
            tmp = two_color
            two_color = (two_color * 3 + three_color * 2) % 1000000007
            # ((two_color / 6) * 3 + (three_color / 6) * 2) * 6
            three_color = (tmp * 2 + three_color * 2) % 1000000007
            # ((two_color / 6) * 2 + (three_color / 6) * 2) * 6
        return (two_color + three_color) % 1000000007