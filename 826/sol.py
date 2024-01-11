from collections import deque
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dq = deque()
        dq.append((-1, 0))
        sum_ = 0
        ans = float("inf")
        for i, num in enumerate(nums):
            sum_ += num
            while(dq and sum_ <= dq[-1][1]):
                dq.pop()
            while(dq and sum_ - dq[0][1] >= k):
                ans = min(ans, i - dq.popleft()[0])
            dq.append((i, sum_))
        if ans == float("inf"):
            return -1
        return ans