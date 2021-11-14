class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        require = tickets[k]
        for i, ele in enumerate(tickets):
            if i == k:
                ans += require
            elif i < k:
                ans += min(tickets[i], require)
            else:
                ans += min(tickets[i], require - 1)
        return ans
