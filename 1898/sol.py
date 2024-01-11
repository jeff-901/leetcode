class Solution(object):
    def maximumRemovals(self, s, p, removable):
        """
        :type s: str
        :type p: str
        :type removable: List[int]
        :rtype: int
        """
        left = 0
        right = len(removable)
        m = len(p)
        n = len(s)
        while(left <= right):
            mid = (left + right) // 2
            remove = set(removable[:mid])
            i = 0
            j = 0
            while(j < m and i < n):
                if i not in remove and s[i] == p[j]:
                    j += 1
                i += 1
            if j == m:
                left = mid + 1
            else:
                right = mid - 1
        return right