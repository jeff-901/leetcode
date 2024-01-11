class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        push_idx = 0
        l = len(pushed)
        for ele in popped:
            if len(stack) == 0 or stack[-1] != ele:
                while(push_idx < l and pushed[push_idx] != ele):
                    stack.append(pushed[push_idx])
                    push_idx += 1
                push_idx += 1
                if push_idx == l + 1:
                    return False
            else:
                stack.pop()
        return True