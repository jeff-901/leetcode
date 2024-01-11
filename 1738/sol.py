class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n-1):
                matrix[i][j+1] ^= matrix[i][j]
        for j in range(n):
            for i in range(m-1):
                matrix[i+1][j] ^= matrix[i][j]
        # print(matrix)
        min_heap = []
        for i in range(m):
            for j in range(n):
                if len(min_heap) < k:
                    heapq.heappush(min_heap, matrix[i][j])
                elif min_heap[0] < matrix[i][j]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, matrix[i][j])
        return min_heap[0]