class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        ans = 0
        n = len(statements)
        for i in range(1, 2**n):
            m = bin(i)[2:].count("1")
            if m <= ans:
                continue
            good_people = set()
            for j in range(n):
                if i & (1<<j):
                    good_people.add(j)
            valid = True
            for good_person in good_people:
                for j in range(n):
                    if (statements[good_person][j] == 0 and j in good_people) or \
                    (statements[good_person][j] == 1 and j not in good_people):
                        valid = False
                        
                        break
                if not valid:
                    break
            if valid:
                ans = m
        return ans