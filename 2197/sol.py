class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def gcd(a,b): 
            if(b==0): 
                return a 
            else: 
                return gcd(b,a%b) 
        stack = []
        for num in nums:
            while(stack and gcd(stack[-1], num) > 1):
                num = stack[-1] * num // gcd(stack[-1], num)
                stack.pop()
            stack.append(num)
        return stack