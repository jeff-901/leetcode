class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        arr = [(float(w)/q, q) for q, w in zip(quality, wage)]
        arr.sort()
        total_q = 0
        taken = []
        for i in range(k):
            taken.append(-arr[i][1])
            total_q += arr[i][1]
        heapq.heapify(taken)
        ans = total_q * arr[k-1][0]
        for i in range(k, len(wage)):
            total_q += heapq.heappop(taken)
            total_q += arr[i][1]
            heapq.heappush(taken, -arr[i][1])
            ans = min(ans, total_q * arr[i][0])
        return ans