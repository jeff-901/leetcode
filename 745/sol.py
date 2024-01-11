class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        vis = set()
        self.pref = {"#": set()}
        self.suff = {"#": set()}
        for i in range(len(words)-1, -1, -1):
            word = words[i]
            if word in vis:
                continue
            vis.add(word)
            cur = self.pref
            cur["#"].add(i)
            for c in word:
                if c not in cur:
                    cur[c] = {"#": set()}
                cur = cur[c]
                cur["#"].add(i)
            cur = self.suff
            for c in reversed(word):
                if c not in cur:
                    cur[c] = {"#": set()}
                cur = cur[c]
                cur["#"].add(i)

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        cur = self.pref
        for c in pref:
            if c not in cur:
                return -1
            cur = cur[c]
        pref_set = cur["#"]
        cur = self.suff
        for c in reversed(suff):
            if c not in cur:
                return -1
            cur = cur[c]
        suff_set = cur["#"]
        union_set = pref_set & suff_set
        if union_set:
            return max(union_set)
        else:
            return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)