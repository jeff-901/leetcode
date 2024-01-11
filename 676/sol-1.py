class MagicDictionary(object):

    def __init__(self):
        self.length = set()
        self.words = []
        

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        self.words = dictionary
        for word in dictionary:
            self.length.add(len(word))
        
        

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        if len(searchWord) not in self.length:
            return False
        l = len(searchWord)
        for word in self.words:
            if len(word) != l: continue
            count = 0
            for i in range(l):
                if word[i] != searchWord[i]:
                    count += 1
                if count > 1: break
            if count == 1:
                return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)