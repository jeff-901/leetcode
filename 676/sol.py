class MagicDictionary(object):

    def __init__(self):
        self.length = set()
        self.root = {}
        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            self.length.add(len(word))
            cur = self.root
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[""] = {}
        
        

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        if len(searchWord) not in self.length:
            return False
        def find(node, word, cnt):
            if word == "":
                if cnt == 0 and "" in node:
                    return True
                else:
                    return False
            if cnt == 0:
                if word[0] in node:
                    return find(node[word[0]], word[1:], 0)
                else:
                    return False
            else:
                if word[0] in node and find(node[word[0]], word[1:], 1):
                    return True
                for ele in node:
                    if ele == word[0]: continue
                    if find(node[ele], word[1:], 0): return True
        return find(self.root, searchWord, 1)
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)