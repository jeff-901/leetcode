class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        q = [0, 0, 0]
        for stone in stones:
            q[stone % 3] += 1
        if q[1] == 0:
            return (q[2] > 2 and q[0] % 2)
        if q[2] == 0:
            return (q[1] > 2 and q[0] % 2)
        if q[0] % 2 == 0:
            return True # choose smaller group
        else:
            #if q[1] - 1 > q[2]+1 or q[2] - 1 > q[1]+1:
            #    return True
            return abs(q[1] - q[2]) > 2