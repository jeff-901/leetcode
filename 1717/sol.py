class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        if x > y:
            pre_a = 0
            pre_b = 0
            for c in s:
                if c == "a":
                    pre_a += 1
                elif c == "b":
                    if pre_a:
                        pre_a -= 1
                        ans += x
                    else:
                        pre_b += 1
                else:
                    ans += min(pre_a, pre_b) * y
                    pre_a = 0
                    pre_b = 0
            ans += min(pre_a, pre_b) * y
        else:
            pre_a = 0
            pre_b = 0
            for c in s:
                if c == "a":
                    if pre_b:
                        pre_b -= 1
                        ans += y
                    else:
                        pre_a += 1
                elif c == "b":
                    pre_b += 1
                else:
                    ans += min(pre_a, pre_b) * x
                    pre_a = 0
                    pre_b = 0
            ans += min(pre_a, pre_b) * x
        return ans
