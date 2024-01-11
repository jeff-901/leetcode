class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {"sum": 0}
                cur = cur[c]
                cur["sum"] += 1
        ans = []
        for word in words:
            cnt = 0
            cur = trie
            for c in word:
                cur = cur[c]
                cnt += cur["sum"]
            ans.append(cnt)
        return ans
        