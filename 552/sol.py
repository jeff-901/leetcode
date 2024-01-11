class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        A0L0 = 1
        A0L1 = 1
        A0L2 = 0
        A1L0 = 1
        A1L1 = 0
        A1L2 = 0
        mod = 1000000007
        for _ in range(1, n):
            tmp_A1L2 = A1L2
            A1L2 = A1L1
            A1L1 = A1L0
            A1L0 = (A1L0 + A0L0 + A0L1 + A0L2 + tmp_A1L2 + A1L2) % mod
            tmp_A0L2 = A0L2
            tmp_A0L1 = A0L1
            A0L2 = A0L1
            A0L1 = A0L0
            A0L0 = (A0L0 + tmp_A0L1 + tmp_A0L2) % mod
            # print(A0L0, A0L1, A0L2, A1L0, A1L1, A1L2)
        return (A0L0 + A0L1 + A0L2 + A1L0 + A1L1 + A1L2) % mod