class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        last = set()
        for num in arr:
            last = {num|q for q in last}
            last.add(num)
            res.update(last)
        return len(res)