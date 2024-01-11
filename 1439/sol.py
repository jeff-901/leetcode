import heapq
class Solution(object):
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(mat)
        output_row = mat[0][:k]
        n = len(mat[0])
        min_hp = []
        for row_idx in range(1, m):
            first_row = output_row[:]
            second_row = mat[row_idx]
            output_len = 0
            min_hp = []
            output_row = []
            for i in range(len(first_row)):
                min_hp.append((first_row[i] + second_row[0], i, 0))
            while(output_len < k and min_hp):
                val, i, j = heapq.heappop(min_hp)
                output_row.append(val)
                if j + 1 < n:
                    heapq.heappush(min_hp, (first_row[i] + second_row[j+1], i, j+1))
                output_len += 1
        return output_row[-1]

            


