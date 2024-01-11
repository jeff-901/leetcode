class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        c_stack = []
        num_stack = []
        for c in s:
            if c_stack and c_stack[-1] == c:
                if num_stack[-1] != k-1:
                    num_stack[-1] += 1
                else:
                    num_stack.pop()
                    c_stack.pop()
            else:
                c_stack.append(c)
                num_stack.append(1)
        ans = ""
        for i in range(len(c_stack)):
            ans += c_stack[i] * num_stack[i]
        return ans