from collections import deque
class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dq = deque()
        dq.append((0, nums[0]))
        for i in range(1, len(nums)):
            if i - dq[0][0] > k:
                dq.popleft()
            cur = nums[i] + dq[0][1]
            while(dq and dq[-1][1] <= cur):
                dq.pop()
            dq.append((i, cur))
        return dq[-1][1]