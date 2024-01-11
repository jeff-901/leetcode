from collections import deque
class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        dq = deque()
        ans = [-1 for _ in range(len(cars))]
        for i in range(len(cars)-1, -1, -1):
            pos, speed = cars[i]
            while(dq and cars[dq[-1]][1] >= speed):
                dq.pop()
            while(dq):
                time_to_collide = float(cars[dq[-1]][0] - pos) / (speed - cars[dq[-1]][1])
                if ans[dq[-1]] == -1 or time_to_collide <= ans[dq[-1]]:
                    ans[i] = time_to_collide
                    break
                dq.pop()
            dq.append(i)
            #print(dq)
        return ans

