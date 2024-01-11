class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        t_cnt = set()
        for c in target:
            t_cnt.add(c)
        for i, sticker in enumerate(stickers):
            cnt = {}
            for c in sticker:
                if c in t_cnt:
                    cnt[c] = cnt.get(c, 0) + 1
            stickers[i] = cnt
        memo = {"": 0}
        def dp(target):
            if target in memo:
                return memo[target]
            min_cost = 51
            for sticker in stickers:
                if target[0] not in sticker:
                    continue
                newtarget = target
                for c in sticker:
                    newtarget = newtarget.replace(c, "", sticker[c])
                if newtarget != target:
                    min_cost = min(min_cost, 1 + dp(newtarget))
            memo[target] = min_cost
            return memo[target]
            
        return -1 if dp(target) == 51 else dp(target)
