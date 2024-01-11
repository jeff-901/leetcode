class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parents = [i for i in range(n+1)]
        def find(idx):
            if parents[idx] == idx:
                return idx
            parents[idx] = find(parents[idx])
            return parents[idx]
        ans = []
        for u, v in edges:
            if parents[v] != v:
                ans = [[parents[v], v], [u, v]]
            parents[v] = u
        parents = [i for i in range(n+1)]
        for u, v in edges:
            if len(ans) > 0 and u == ans[1][0] and v == ans[1][1]: continue
            if find(u) == find(v):
                if len(ans) == 0:
                    return u, v
                else:
                    return ans[0]
            parents[v] = u
        return ans[1]