import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = {}
        for ele in s:
            cnt[ele] = cnt.get(ele, 0) + 1
        ans = ""
        heap = []
        for key in cnt:
            heap.append((-cnt[key], key)) 
        heapq.heapify(heap)
        while(heap):
            val1, c1 = heapq.heappop(heap)
            ans += c1
            val1 += 1
            if not heap:
                if val1 == 0:
                    return ans
                return ""
            val2, c2 = heapq.heappop(heap)
            ans += c2
            val2 += 1
            if val1 < 0:
                heapq.heappush(heap, (val1, c1))
            if val2 < 0:
                heapq.heappush(heap, (val2, c2))
        return ans