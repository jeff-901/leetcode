class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for ele in s:
            if ele == "(":
                stack.append(-1)
            else:
                score = 0
                if stack[-1] > 0:
                    score = stack.pop()
                    score *= 2
                else:
                    score = 1
                stack.pop()
                if len(stack) > 0 and stack[-1] > 0:
                    stack.append(stack.pop() + score)
                else:
                    stack.append(score)
        return stack[-1]