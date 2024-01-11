class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        diff = abs(a - b)
        if a > b:
            if diff > b:
                return "aab" * b + "a" * (a - 2*b)
            else:
                return "aab" * diff + "ab" * (b - diff)
        else:
            if diff > a:
                return "bba" * a + "b" * (b - 2*a)
            else:
                return "bba" * diff + "ba" * (a - diff)