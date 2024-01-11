import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        max_hp = []
        pos = startFuel
        ans = 0
        station_idx = 0
        while(pos < target):
            while(station_idx < len(stations) and stations[station_idx][0] <= pos):
                heapq.heappush(max_hp, (-stations[station_idx][1]))
                station_idx += 1
            if not max_hp:
                return -1
            pos += -heapq.heappop(max_hp)
            ans += 1
        return ans