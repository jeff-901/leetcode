class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        n = len(parent)
        self.children = [[] for _ in range(n)]
        for c, p in enumerate(parent):
            if p == -1:
                continue
            self.children[p].append(c)
        self.ans = 1
        def dfs(node):
            first_max = 0
            second_max = 0
            for c in self.children[node]:
                r = dfs(c)
                if s[c] != s[node]:
                    if r > first_max:
                        second_max = first_max
                        first_max = r
                    elif r > second_max:
                        second_max = r
            self.ans = max(self.ans, first_max + second_max + 1)
            return first_max + 1
        dfs(0)
        return self.ans
        