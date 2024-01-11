class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        radius = 0
        m = len(heaters)
        j = 0
        for house in houses:
            while(j < m - 1 and house > heaters[j]):
                j += 1
            if j == 0:
                radius = max(radius, abs(heaters[j] - house))
            else:
                radius = max(radius, min(abs(heaters[j] - house), house - heaters[j-1]))
        return radius