import heapq
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        m = len(tasks)
        ans = []
        running = []
        available = []
        for i, s in enumerate(servers):
            available.append((s, i))
        heapq.heapify(available)
        t = 0
        task_idx = 0
        while(task_idx < m):
            while(running and running[0][0] <= t):
                _, idx = heapq.heappop(running)
                heapq.heappush(available, (servers[idx], idx))
            if not available:
                t = running[0][0]
            else:
                while(task_idx <= t and task_idx < m and available):
                    s, idx = heapq.heappop(available)
                    ans.append(idx)
                    heapq.heappush(running, (t + tasks[task_idx], idx))
                    task_idx += 1
                t += 1
        return ans
