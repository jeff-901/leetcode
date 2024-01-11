class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0 for _ in range(26)]
        l = len(s)
        for ele in s:
            cnt[ord(ele) - 97] += 1
        max_idx = 0
        max_cnt = 0
        for i in range(26):
            if cnt[i] > max_cnt:
                max_cnt = cnt[i]
                max_idx = i
        if max_cnt > (l+1) // 2:
            return ""
        ans = [chr(97+max_idx) for _ in range(l)]
        cnt[max_idx] = 0
        idx = 1
        for i in range(26):
            for _ in range(cnt[i]):
                ans[idx] = chr(97+i)
                idx += 2
                if idx >= l:
                    idx = 0
        return "".join(ans)