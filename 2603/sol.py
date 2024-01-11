class Solution(object):
    def collectTheCoins(self, coins, edges):
        """
        :type coins: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(coins)
        degree = [set() for _ in range(n)]
        count = [0 for _ in range(n)]
        m = len(edges)
        for u, v in edges:
            degree[u].add(v)
            degree[v].add(u)
        queue = []
        for i in range(n):
            if len(degree[i]) == 1:
                queue.append(i)
        while(queue):
            cur = queue.pop()
            if len(degree[cur]) == 0: continue
            neighbor = list(degree[cur])[0]
            degree[neighbor].remove(cur)
            if coins[cur] == 0:
                if count[cur] == 1:
                    count[neighbor] = 2
                elif count[neighbor] < 2 and len(degree[neighbor]) == 1:
                    queue.append(neighbor)
            else:
                count[neighbor] = max(count[neighbor], count[cur] + 1)
                if count[neighbor] < 2 and len(degree[neighbor]) == 1:
                    queue.append(neighbor)
            m -= 1
        return m * 2