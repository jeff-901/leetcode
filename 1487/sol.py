class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        cnt = {}
        seen = set()
        ans = []
        for name in names:
            if name in seen:
                k = 1
                if name in cnt:
                    k = cnt[name]
                while(True):
                    modified = "{}({})".format(name, k)
                    if modified not in seen:
                        cnt[name] = k + 1
                        name = modified
                        break
                    k += 1
            ans.append(name)
            seen.add(name)
        return ans
