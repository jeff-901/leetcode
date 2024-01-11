from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        ans = []
        for i in range(0, min(k, len(nums))):
            while len(dq) > 0 and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])
        
        for j in range(k, len(nums)):
            if dq[0] <= j-k:
                dq.popleft()
            while len(dq) > 0  and nums[j] >= nums[dq[-1]]:
                dq.pop()
            dq.append(j)
            ans.append(nums[dq[0]])
        return ans
            
            