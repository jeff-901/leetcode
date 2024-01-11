class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = 0
        for ele in s:
            if ele == "(":
                stack.append(-1)
            elif ele == ")":
                cur_longest = 0
                if len(stack) > 0 and stack[-1] > 0:
                    cur_longest = stack.pop()
                if len(stack) > 0 and stack[-1] == -1:
                    stack.pop()
                    if len(stack) > 0 and stack[-1] > 0:
                        cur_longest += stack.pop()
                    cur_longest += 2
                    ans = max(ans, cur_longest)
                    stack.append(cur_longest)
                else:
                    while(len(stack) > 0):
                        stack.pop()
        return ans
        