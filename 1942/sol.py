import heapq
class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        n = len(times)
        free_chair = [_ for _ in range(n)]
        occupied = []
        friends = [(a, l, idx) for idx, (a, l) in enumerate(times)]
        friends.sort()
        for a, l, idx in friends:
            while(occupied and occupied[0][0] <= a):
                _, chair_num = heapq.heappop(occupied)
                heapq.heappush(free_chair, chair_num)
            chair_num = heapq.heappop(free_chair)
            if idx == targetFriend:
                return chair_num
            heapq.heappush(occupied, (l, chair_num))