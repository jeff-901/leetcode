class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = []
        for i, num in enumerate(nums):
            while(stack and nums[stack[-1]] < num):
                ans[stack.pop()] = num
            stack.append(i)
            ans.append(-1)
        for num in nums:
            while(stack and nums[stack[-1]] < num):
                ans[stack.pop()] = num
        return ans