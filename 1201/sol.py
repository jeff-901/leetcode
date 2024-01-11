class Solution(object):
    def nthUglyNumber(self, n, a, b, c):
        """
        :type n: int
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        def gcd(a,b): 
            if(b==0): 
                return a 
            else: 
                return gcd(b,a%b) 
        left = 1
        right = n * max(a, b, c)
        ab = a*b//gcd(a,b)
        bc = b*c//gcd(b,c)
        ac = a*c//gcd(a,c)
        abc = ac*b//gcd(ac, b)
        while(left <= right):
            mid = (left + right) // 2
            cnt = (mid // a) + (mid // b) + (mid // c) - (mid // ab) - (mid // bc) - (mid // ac) + (mid // abc)
            if cnt < n:
                left = mid + 1
            else:
                right = mid - 1
        return left