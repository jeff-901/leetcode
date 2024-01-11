class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        n_str = str(n)
        bit = len(n_str)
        m = len(digits)
        if m != 1:
            ans = ((m**bit - 1) // (m - 1)) - 1
        else:
            ans = bit - 1
        digits = [int(ele) for ele in digits]
        for i in range(bit, 0, -1):
            biggest = int(n_str[bit-i])
            cnt = 0
            same = False
            for num in digits:
                if num < biggest:
                    cnt += 1
                elif num == biggest:
                    same = True
            ans += cnt * ( m ** (i - 1))
            if not same:
                break
        if same:
            ans += 1
        return ans