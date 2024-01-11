class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        cur = 0
        h = {0: [1, 0]}
        for i, num in enumerate(arr):
            cur ^= num
            if cur in h:
                ans += i * h[cur][0] - h[cur][1]
                h[cur][0] += 1
                h[cur][1] += i + 1
            else:
                h[cur] = [1, i + 1]
        return ans