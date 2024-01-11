class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        self.d = {}
        for a, b in edges:
            if a in self.d:
                self.d[a].append(b)
            else:
                self.d[a] = [b]
            if b in self.d: 
                self.d[b].append(a)
            else:
                self.d[b] = [a]
        self.seen = set()
        def dfs(node, d):
            #return (bob step, award)
            res = -float("inf")
            self.seen.add(node)
            bob_step = float("inf")
            for neighbor in self.d[node]:
                if neighbor in self.seen:
                    continue
                cur, val = dfs(neighbor, d+1)
                bob_step = min(bob_step, cur)
                res = max(res, val)
            if res == -float("inf"):
                res = 0
            if node == bob:
                bob_step = 0
    
            if bob_step == d:
                res += amount[node] // 2
            elif bob_step > d:
                res += amount[node]
            return (bob_step + 1, res)
        _, ans = dfs(0, 0)
        return ans
