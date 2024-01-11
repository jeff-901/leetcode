class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        arr = [[a, "a"], [b, "b"], [c, "c"]]
        total = a + b + c
        arr.sort()
        left = arr[0][0] + arr[1][0]
        max_available = left * 2 + 2
        if max_available < arr[2][0]:
            l = left + max_available
            max_cnt = max_available
        else:
            l = total
            max_cnt = arr[2][0]

        ans = [arr[2][1] for _ in range(l)]
        end_idx_of_smallest = 2 + 3 * arr[0][0]
        for i in range(2, end_idx_of_smallest, 3):
            ans[i] = arr[0][1]
        for i in range(end_idx_of_smallest, l, 3):
            ans[i] = arr[1][1]
        arr[1][0] -= (l - end_idx_of_smallest + 2) // 3
        for i in range(1, 1 + 3 * arr[1][0], 3):
            ans[i] = arr[1][1]
        return "".join(ans)