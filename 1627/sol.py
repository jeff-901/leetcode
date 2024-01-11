class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        parents = [_ for _ in range(n+1)]
        def find(idx):
            if parents[idx] == idx: 
                return idx
            parents[idx] = find(parents[idx])
            return parents[idx]
        for i in range(threshold+1, n):
            if parents[i] != i: continue
            for num in range(2*i, n+1, i):
                i_p = find(i)
                num_p = find(num)
                if i_p != num_p:
                    parents[i_p] = num_p
        ans = []
        for a, b in queries:
            ans.append(find(a) == find(b))
        return ans 
            
        