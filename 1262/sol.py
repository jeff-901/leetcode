class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = sum(nums) % 1000000007
        remain = ans % 3
        if remain == 0:
            return ans
        a1 = [10003, 10006]
        a2 = [10001, 10004]
        a1cnt = 0
        a2cnt = 0
        for num in nums:
            if num % 3 == 1:
                if num < a1[0]:
                    a1[1] = a1[0]
                    a1[0] = num
                elif num < a1[1]:
                    a1[1] = num
                a1cnt += 1
            elif num % 3 == 2:
                if num < a2[0]:
                    a2[1] = a2[0]
                    a2[0] = num
                elif num < a2[1]:
                    a2[1] = num
                a2cnt += 1
        if remain == 2:
            if a2cnt == 0:
                ans = (ans - sum(a1)) % 1000000007
            elif a1cnt < 2:
                ans = (ans - a2[0]) % 1000000007
            else:
                ans = (ans - min(a2[0], sum(a1))) % 1000000007
        else:
            if a1cnt == 0:
                ans = (ans - sum(a2)) % 1000000007
            elif a2cnt < 2:
                ans = (ans - a1[0]) % 1000000007
            else:
                ans = (ans - min(a1[0], sum(a2))) % 1000000007
        return ans