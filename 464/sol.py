class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        total = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if total < desiredTotal:
            return False
        elif total == desiredTotal:
            return maxChoosableInteger % 2
        h = {}
        def check_win(choices, key, remain):
            if choices[-1] >= remain:
                return True
            if key in h:
                return h[key]
            for i in range(len(choices)):
                if not check_win(choices[:i] + choices[i+1:], key ^ (1 << (choices[i]-1)), remain - choices[i]):
                    h[key] = True
                    return True
            h[key] = False
            return False 
        
        return check_win(list(range(1, maxChoosableInteger+1)), 2**maxChoosableInteger - 1, desiredTotal)