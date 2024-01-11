import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        taken = []
        t = 0
        for duration, end_t in sorted(courses, key = lambda x: x[1]):
            if t + duration <= end_t:
                t += duration
                heapq.heappush(taken, -duration)
            else:
                if taken and -taken[0] > duration:
                    t += heapq.heappop(taken) + duration
                    heapq.heappush(taken, -duration)
        return len(taken)