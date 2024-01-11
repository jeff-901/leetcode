class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        remain = sum(digits) % 3
        a1 = [10003, 10006]
        a2 = [10001, 10004]
        a1cnt = 0
        a2cnt = 0
        if remain != 0:
            for digit in digits:
                if digit % 3 == 1:
                    if digit < a1[0]:
                        a1[1] = a1[0]
                        a1[0] = digit
                    elif digit < a1[1]:
                        a1[1] = digit
                    a1cnt += 1
                elif digit % 3 == 2:
                    if digit < a2[0]:
                        a2[1] = a2[0]
                        a2[0] = digit
                    elif digit < a1[1]:
                        a2[1] = digit
                    a2cnt += 1
            if remain == 1:
                if a1cnt > 0:
                    digits.remove(a1[0])
                else:
                    digits.remove(a2[0])
                    digits.remove(a2[1])
            if remain == 2:
                if a2cnt > 0:
                    digits.remove(a2[0])
                else:
                    digits.remove(a1[0])
                    digits.remove(a1[1])
        digits.sort(reverse=True)
        if len(digits) == 0:
            return ""
        
        return str(int("".join([str(d) for d in digits])))
        