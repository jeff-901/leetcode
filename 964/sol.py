class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        h = {}
        def back(target):
            if target < x:
                return min(target * 2 - 1, (x - target) * 2)
            if target in h:
                return h[target]
            bit = 0
            while(x**(bit + 1) <= target):
                bit += 1
            a = target // (x**(bit))
            if a * (x**bit) == target:
                return min(a*bit, (x-a)*bit+bit+1) - 1
            ans = min(min(a*bit, (x-a)*bit+bit+1) + back(abs(target - a * (x**bit))), \
            min((a+1)*bit, (x-a-1)*bit+bit+1)+back(abs((a+1)*(x**bit) - target)))
            h[target] = ans
            return ans
        return back(target)