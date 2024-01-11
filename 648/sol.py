class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split(" ")
        root = {}
        def find(node, word):
            if word == "":
                return ""
            if "" in node:
                return ""
            elif word[0] not in node:
                return word
            else:
                return word[0] + find(node[word[0]], word[1:]) 
        for w in dictionary:
            cur = root
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[""] = {} 
        for i in range(len(sentence)):
            sentence[i] = find(root, sentence[i])
        return " ".join(sentence)
