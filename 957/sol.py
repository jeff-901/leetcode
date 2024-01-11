class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        mask = 0
        for c in cells:
            mask <<= 1
            mask |= c
        bit_mask = 2**7 - 2
        bit8_mask = 2**8 - 1
        h = {}
        i = 0
        h[mask] = i
        while n > 0:
            mask = (bit8_mask ^ ((mask << 1) ^ (mask >> 1))) & bit_mask
            i += 1
            n -= 1
            if mask not in h:
                h[mask] = i
            else:
                cycle = i - h[mask]
                n = n % cycle
            
        for i in range(8):
            cells[i] = (mask >> (8 - i - 1)) & 1
        return cells