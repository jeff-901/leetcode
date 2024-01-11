class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        part = [0 for _ in range(n)]
        for i in range(n):
            if part[i] == 0:
                part[i] = 1
                queue = [i]
                while(queue):
                    cur = queue.pop()
                    for ele in graph[cur]:
                        if part[ele] == 0:
                            part[ele] = part[cur] * -1
                            queue.append(ele)
                        elif part[ele] == part[cur]:
                            return False
        return True
            
        