class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        ans = -1
        for i in range(len(edges)):
            if edges[i] == -1: continue
            cnt = 0
            vis = {}
            cur = i
            while(cur != -1 and cur not in vis):
                vis[cur] = cnt
                cnt += 1
                next_cur = edges[cur]
                edges[cur] = -1
                cur = next_cur
            if cur != -1:
                ans = max(ans, cnt - vis[cur])
        return ans