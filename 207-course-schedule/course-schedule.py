class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False  # cycle detected
            if course in visited:
                return True   # already checked

            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True