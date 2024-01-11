class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0 for _ in temperatures]
        stack = []
        for idx in range(len(temperatures)):
            while(len(stack) > 0 and temperatures[idx] > temperatures[stack[-1]]):
                past_idx = stack.pop()
                ans[past_idx] = idx - past_idx
            stack.append(idx)
        return ans