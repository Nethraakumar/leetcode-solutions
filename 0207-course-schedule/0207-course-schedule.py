from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Build graph
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # Start with nodes having no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        taken = 0

        while queue:
            course = queue.popleft()
            taken += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return taken == numCourses