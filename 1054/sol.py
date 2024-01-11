class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        cnt = {}
        l = len(barcodes)
        max_cnt = 0
        max_ele = None
        for ele in barcodes:
            cnt[ele] = cnt.get(ele, 0) + 1
        for ele in cnt:
            if cnt[ele] > max_cnt:
                max_ele = ele
                max_cnt = cnt[ele]
        ans = [max_ele for _ in range(l)]
        del cnt[max_ele]
        idx = 1
        for ele in cnt:
            for i in range(cnt[ele]):
                ans[idx] = ele
                idx += 2
                if idx >= l:
                    idx = 0
        return ans
    