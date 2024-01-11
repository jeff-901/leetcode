class MapSum(object):

    def __init__(self):
        self.root = {}        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        def add(node, key):
            if key == "":
                diff = val - node.get("", 0)
                node[""] = val
                return diff
            if key[0] not in node:
                node[key[0]] = {"sum": 0}
            node = node[key[0]]
            diff = add(node, key[1:])
            node["sum"] += diff
            return diff
        add(self.root, key)
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        # print(self.root)
        cur = self.root
        for c in prefix:
            if c not in cur:
                return 0
            cur = cur[c]
        return cur["sum"]
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)