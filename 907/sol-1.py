class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        pre_sum = 0
        for idx, num in enumerate(arr):
            if len(stack) == 0 or arr[stack[-1][0]] < num:
                pre_sum = (pre_sum + num) % 1000000007
                ans = (ans + pre_sum) % 1000000007
                stack.append([idx, num])
            else:
                while(len(stack) > 0 and arr[stack[-1][0]] > num):
                    pre_sum -= stack.pop()[1]
                if len(stack) == 0:
                    stack.append([idx, num*(idx + 1)])
                else:
                    stack.append([idx, num*(idx - stack[-1][0])])
                pre_sum = (pre_sum + stack[-1][1]) % 1000000007
                ans = (ans + pre_sum) % 1000000007
        return ans
