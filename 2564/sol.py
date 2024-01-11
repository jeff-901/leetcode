class Solution(object):
    def substringXorQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(s)
        h = {}
        for start in range(n):
            if s[start] == "0":
                if 0 not in h:
                    h[0] = [start, start]
            else:
                val = 0
                for i in range(min(31, n-start)):
                    val = val * 2 + int(s[start+i])
                    if val not in h:
                        h[val] = [start, start+i]
        for i in range(len(queries)):
            first, second = queries[i]
            queries[i] = h.get(first^second, [-1, -1])
        return queries

