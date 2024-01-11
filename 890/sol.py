class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        l = len(pattern)
        for word in words:
            if len(word) != len(pattern):
                continue
            h = {}
            valid = True
            for i in range(l):
                if word[i] in h:
                    if h[word[i]] != pattern[i]:
                        valid = False
                        break
                else:
                    h[word[i]] = pattern[i]
            vis = 0
            for ele in h:
                bit_val = 1 << (ord(h[ele]) - ord('a'))
                if vis & bit_val != 0:
                    valid = False
                    break
                vis |= bit_val
            if valid:
                ans.append(word)
        return ans
                