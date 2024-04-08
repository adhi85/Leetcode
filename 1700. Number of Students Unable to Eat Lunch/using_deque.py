from collections import deque


class Solution:
    def countStudents(self, students, sandwiches) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)

        while students:

            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                j = len(students)

                while j:
                    val = students.popleft()
                    students.append(val)

                    if students[0] == sandwiches[0]:
                        students.popleft()
                        sandwiches.popleft()
                        break

                    j -= 1
                if j == 0:
                    return len(students)

        return 0
