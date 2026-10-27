from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph =[[] for _ in range(n)]
        req_deg =[0]*n
        for c,p in prerequisites:
            graph[p].append(c)
            req_deg[c] +=1
        queue = deque()
        for i in range(n):
            if req_deg[i] == 0:
                queue.append(i)

        c_t = 0
        while queue:
            cou = queue.popleft()
            c_t +=1
            for n_c in graph[cou]:
                req_deg[n_c]-=1
                if req_deg[n_c] == 0:
                    queue.append(n_c)
        return c_t == n