class Solution(object):
    def countHighestScoreNodes(self, parents):
        """
        :type parents: List[int]
        :rtype: int
        """
        self.ans = 0
        self.cnt = 1
        self.n = len(parents)
        self.children = [[] for _ in range(self.n)]
        for c, p in enumerate(parents):
            if p == -1:
                continue
            self.children[p].append(c)
        def dfs(node):
            r = []
            product_r = 1
            total_r = 0
            for c in self.children[node]:
                val = dfs(c)
                product_r *= val
                total_r += val
            score = max(1, self.n - 1 - total_r) * product_r
            if score > self.ans:
                self.ans = score
                self.cnt = 1
            elif score == self.ans:
                self.cnt += 1
            return 1 + total_r
        dfs(0)
        return self.cnt
            