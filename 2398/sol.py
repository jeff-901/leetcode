import collections
class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        total_cost = 0
        dq = collections.deque()
        i = 0
        n = len(chargeTimes)
        for j in range(n):
            while(dq and chargeTimes[dq[-1]] <= chargeTimes[j]):
                dq.pop()
            dq.append(j)
            total_cost += runningCosts[j]
            if chargeTimes[dq[0]] + (j - i + 1) * total_cost > budget:
                if dq[0] == i:
                    dq.popleft()
                total_cost -= runningCosts[i]
                i += 1
        return n - i