class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(2**len(requests)):
            net_out = [0] * n
            net_in = [0] * n
            cnt = bin(i)[2:].count("1")
            if cnt <= ans:
                continue
            for j, (fr, to) in enumerate(requests):
                if i & (1 << j):
                    net_out[fr] += 1
                    net_in[to] += 1
            equal = True
            for j in range(n):
                if net_out[j] != net_in[j]:
                    equal = False
                    break
            if equal:
                ans = max(ans, cnt)
        return ans