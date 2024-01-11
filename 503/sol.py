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
                ans[stack.pop()] = i
            stack.append(i)
            ans.append(-1)
        cur = 0
        while(stack):
            while cur != -1 and nums[cur] <= nums[stack[-1]]:
                cur = ans[cur]
            if cur == -1:
                break
            ans[stack.pop()] = cur
        for i in range(len(ans)):
            if ans[i] != -1:
                ans[i] = nums[ans[i]]
        return ans