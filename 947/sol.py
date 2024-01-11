class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        n = len(stones)
        parents = [i for i in range(n)]
        row = {}
        col = {}
        for i, (r, c) in enumerate(stones):
            if r not in row:
                row[r] = [i]
            else:
                row[r].append(i)
            if c not in col:
                col[c] = [i]
            else:
                col[c].append(i)
        def find(idx):
            if parents[idx] == idx:
                return idx
            parents[idx] = find(parents[idx])
            return parents[idx]
        for ele in row:
            cur = row[ele][0]
            for j in range(1, len(row[ele])):
                cur_p = find(cur)
                next_p = find(row[ele][j])
                if cur_p != next_p:
                    parents[next_p] = cur_p
        for ele in col:
            cur = col[ele][0]
            for j in range(1, len(col[ele])):
                cur_p = find(cur)
                next_p = find(col[ele][j])
                if cur_p != next_p:
                    parents[next_p] = cur_p
        ans = 0
        for i in range(n):
            if parents[i] == i:
                ans += 1
        return n - ans