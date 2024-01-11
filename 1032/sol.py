class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = {}
        for word in words:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = {}
        self.queue = []
        
        

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        tmp = []
        ans = False
        for node in self.queue:
            if letter in node:
                next_node = node[letter]
                if "#" in next_node:
                    ans = True
                tmp.append(next_node)
        if letter in self.trie:
            tmp.append(self.trie[letter])
            if "#" in self.trie[letter]:
                ans = True
        self.queue = tmp
        return ans
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)