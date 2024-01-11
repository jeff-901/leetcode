import heapq
class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        available = []
        for idx, server in enumerate(servers):
            available.append((server, idx, 0))
        heapq.heapify(available)
        assigned = []
        
        ans = []

        for i in range(len(tasks)):
            while (assigned and assigned[0][0] <= i) or not available:
                last_end_time, weight, server_idx = heapq.heappop(assigned)
                heapq.heappush(available, (weight, server_idx, last_end_time))
            weight, server_idx, last_end_time = heapq.heappop(available)
            ans.append(server_idx)
            end_time = max(i, last_end_time) + tasks[i]
            heapq.heappush(assigned, (end_time, weight, server_idx))
        return ans