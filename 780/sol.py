class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while(sx < tx and sy < ty):
            if ty > tx:
                ty = ty % tx
            else:
                tx = tx % ty
        return (sx == tx and sy <= ty and (ty - sy) % sx == 0) or \
          (sy == ty and sx <= tx and (tx - sx) % sy == 0)