class WordDictionary(object):

    def __init__(self):
        self.root = {}
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[""] = {}
        
    

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def find(node, word):
            if word == "":
                return word in node
            if word[0] == ".":
                for ele in node:
                    if find(node[ele], word[1:]):
                        return True
            else:
                return word[0] in node and find(node[word[0]], word[1:])
        return find(self.root, word)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)