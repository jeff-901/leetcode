class Solution(object):
    def friendRequests(self, n, restrictions, requests):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :type requests: List[List[int]]
        :rtype: List[bool]
        """
        parents = [_ for _ in range(n)]
        restrict = [set() for _ in range(n)]
        ans = []

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        for a, b in restrictions:
            restrict[a].add(b)
            restrict[b].add(a)

        for a, b in requests:
            ap = find(a)
            bp = find(b)
            flag = True
            for ele in restrict[ap]:
                if find(ele) == bp:
                    ans.append(False)
                    flag = False
                    break
            if flag:
                for ele in restrict[bp]:
                    if find(ele) == ap:
                        ans.append(False)
                        flag = False
                        break
            if flag:
                if ap != bp:
                    parents[ap] = bp
                    for ele in restrict[ap]:
                        restrict[bp].add(ele)
                ans.append(True)

        return ans
