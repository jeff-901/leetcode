class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = (0, 0)
        min_ = len(s)
        t_cnt = {}
        cur_cnt = {}
        for ele in t:
            if ele not in t_cnt:
                t_cnt[ele] = 1
                cur_cnt[ele] = 0
            else:
                t_cnt[ele] += 1
        left = 0
        right = 0
        hit = 0
        while right < len(s):
            ch = s[right]
            if ch in t_cnt:
                cur_cnt[ch] += 1
                if cur_cnt[ch] <= t_cnt[ch]:
                    hit += 1
            if hit == len(t):
                while left < right:
                    if s[left] not in t_cnt:
                        left += 1
                    elif cur_cnt[s[left]] > t_cnt[s[left]]:
                        cur_cnt[s[left]] -= 1
                        left += 1
                    else:
                        if right - left < min_:
                            min_ = right-left
                            ans = (left, right+1)
                        cur_cnt[s[left]] -= 1
                        left += 1
                        hit -= 1
            right += 1
        return s[ans[0]:ans[1]]