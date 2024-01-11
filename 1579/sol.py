class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parents_bob = [_ for _ in range(n)]
        parents_alice = [_ for _ in range(n)]
        def find_bob(u):
            if parents_bob[u] != u:
                parents_bob[u] = find_bob(parents_bob[u])
            return parents_bob[u]
        
        ans = 0
        for t, u, v in edges:
            if t != 3: continue
            u-=1
            v-=1
            u_p = find_bob(u)
            v_p = find_bob(v)
            if u_p == v_p:
                ans += 1
            else:
                parents_bob[u_p] = v_p
        parents_alice = parents_bob[:]
        def find_alice(u):
            if parents_alice[u] != u:
                parents_alice[u] = find_alice(parents_alice[u])
            return parents_alice[u]
        for t, u, v in edges:
            if t != 1: continue
            u-=1
            v-=1
            u_p = find_alice(u)
            v_p = find_alice(v)
            if u_p == v_p:
                ans += 1
            else:
                parents_alice[u_p] = v_p
        p = find_alice(0)
        for i in range(1, n):
            if find_alice(i) != p:
                return -1
        for t, u, v in edges:
            if t != 2: continue
            u-=1
            v-=1
            u_p = find_bob(u)
            v_p = find_bob(v)
            if u_p == v_p:
                ans += 1
            else:
                parents_bob[u_p] = v_p
        p = find_bob(0)
        for i in range(1, n):
            if find_bob(i) != p:
                return -1
        return ans