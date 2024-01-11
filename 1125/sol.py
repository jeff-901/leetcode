class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        h = {}
        cnt = 0
        for req_skill in req_skills:
            h[req_skill] = cnt
            cnt += 1
        req_mask = (1 << len(req_skills)) - 1
        newpeople = []
        for skills in people:
            mask = 0
            for skill in skills:
                if skill in h:
                    mask |= 1 << h[skill]
            newpeople.append(mask)
        memo = {0: []}
        def dp(target, mask):
            if target in memo:
                return memo[target]
            lsb = target & -target
            min_people = 61
            ans = []
            for i, skill_mask in enumerate(newpeople):
                if skill_mask & lsb == 0 or (1 << i) & mask:
                    continue
                new_target = target ^ (target & skill_mask)
                res = dp(new_target, mask | (1 << i))
                if len(res) + 1 < min_people:
                    min_people = len(res) + 1
                    ans = res + [i]
            memo[target] = ans
            return ans
        return dp(req_mask, 0)