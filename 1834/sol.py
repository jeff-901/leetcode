import heapq
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        tasks = sorted([(en, process, idx) for idx, (en, process) in enumerate(tasks)], reverse=True)
        waiting = []
        t = tasks[-1][0]
        ans = []
        while(waiting or tasks):
            if not waiting and t < tasks[-1][0]:
                t = tasks[-1][0]
            while(tasks and tasks[-1][0] <= t):
                _, process_time, idx = tasks.pop()
                heapq.heappush(waiting, (process_time, idx))
            
            process_time, idx = heapq.heappop(waiting)
            ans.append(idx)
            t += process_time
            
        return ans