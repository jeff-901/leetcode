class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        ans = 0
        while(target > startValue):
            if target % 2:
                target = (target + 1) // 2
                ans += 2
            else:
                target //= 2
                ans += 1
        ans += startValue - target
        return ans