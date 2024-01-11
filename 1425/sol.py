from collections import deque
class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = -100000
        dq = deque()
        #dq.append((-1, 0))
        cur_max = 0
        for i, num in enumerate(nums):
            if dq and i - dq[0][0] > k:
                # if (dq[0][0] != -1):
                ans = max(ans, dq.popleft()[1])
                # else:
                #     dq.popleft()
            if dq:
                cur_max = num + max(0, dq[0][1])
            else:
                cur_max = num
            while(dq and dq[-1][1] <= cur_max):
                dq.pop()
            dq.append((i, cur_max))
        ans = max(ans, dq.popleft()[1]) 
        return ans