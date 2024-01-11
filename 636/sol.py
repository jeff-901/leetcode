class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0 for _ in range(n)]
        stack = []
        for log in logs:
            fid, exe_type, t = log.split(":")
            t = int(t)
            if exe_type[0] == "s":
                if len(stack) > 0:
                    stack[-1][1] += t - stack[-1][0]
                stack.append([t, 0])
            else:
                ans[int(fid)] += stack[-1][1] + t - stack[-1][0] + 1
                stack.pop()
                if len(stack) > 0:
                    stack[-1][0] = t + 1
        return ans