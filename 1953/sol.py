class Solution(object):
    def numberOfWeeks(self, milestones):
        """
        :type milestones: List[int]
        :rtype: int
        """
        total = sum(milestones)
        max_num = max(milestones)
        if max_num > (total + 1) // 2:
            return (total - max_num) * 2 + 1
        else:
            return total
