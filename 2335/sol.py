class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        max_num = max(amount)
        ans = (sum(amount) + 1 )// 2
        if max_num > ans:
            return max_num
        else:
            return ans