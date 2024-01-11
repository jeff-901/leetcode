class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverse(s, r):
            ans = ""
            stack = []
            idx = 0
            while(idx < len(s)):
                c = s[idx]
                if c != "(":
                    if r:
                        stack.append(c)
                    else:
                        ans += c
                else:
                    piece = ""
                    idx += 1
                    left_cnt = 1
                    while(True):
                        if s[idx] == "(":
                            left_cnt += 1
                        elif s[idx] == ")":
                            left_cnt -= 1
                        if left_cnt == 0:
                            break
                        piece += s[idx]
                        idx += 1
                    if r:
                        stack.append(reverse(piece, not r))
                    else:
                        ans += reverse(piece, not r)
                idx += 1
            while(stack):
                ans += stack.pop()
            return ans
        return reverse(s, False)