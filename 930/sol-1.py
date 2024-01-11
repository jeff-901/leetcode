from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        ans = 0
        if goal == 0:
            cnt = 0
            for num in nums:
                if num == 0:
                    cnt += 1
                else:
                    ans += (cnt + 1) * cnt // 2
                    cnt = 0
            ans += (cnt + 1) * cnt // 2
            return ans
        left = 1
        left_idx = 0
        sum_ = 0
        for idx, num in enumerate(nums):
            sum_ += num
            if sum_ == goal:
                ans += left
            elif sum_ > goal:
                sum_ -= 1
                left = 1
                left_idx += 1
                while(left_idx < idx and nums[left_idx] == 0):
                    left_idx += 1
                    left += 1
                ans += left
            if sum_ == 0:
                left += 1
                left_idx = idx + 1
        return ans
            

