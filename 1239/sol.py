class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        h = {}
        for s in arr:
            mask = 0
            for ch in s:
                if mask & (1 << ord(ch) - 97):
                    mask = 0
                    break
                mask |= (1 << ord(ch) - 97)
            if mask != 0:
                h[mask] = len(s)
        vis = {0: 0}
        for mask in h:
            last = vis.copy()
            for ele in last:
                if ele & mask == 0:
                    vis[ele | mask] = vis[ele] + h[mask]
            vis[mask] = h[mask]
        return max(vis.values())