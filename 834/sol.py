class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.ans = [0] * n
        root = 0
        self.subtree_node = [0] * n
        self.vis = [0] * n
        adjacent = [[] for _ in range(n)]
        for a, b in edges:
            adjacent[a].append(b)
            adjacent[b].append(a)
        def dfs(node):
            self.vis[node] = 1
            subtree_num = 0
            cost = 0
            for i in adjacent[node]:
                if self.vis[i] == 0:
                    cost += dfs(i) + self.subtree_node[i]
                    subtree_num += self.subtree_node[i]
            self.subtree_node[node] = subtree_num + 1
            return cost
        self.total_cost = dfs(root)
        self.vis = [0] * n
        def cal(node, parent_c):
            self.vis[node] = 1
            if parent_c == -1:
                self.ans[node] = self.total_cost
            else:
                self.ans[node] = parent_c - self.subtree_node[node] + (n - self.subtree_node[node])
            for i in adjacent[node]:
                if self.vis[i] == 0:
                     cal(i, self.ans[node])
        cal(root, -1)
        return self.ans
