class Solution:
    def countStudents(self, students, sandwiches) -> int:

        studentsPreferingOne = 0
        studentsPreferingZero = 0

        for stud in students:
            if stud == 0:
                studentsPreferingZero += 1
            else:
                studentsPreferingOne += 1

        for sandwich in sandwiches:
            if sandwich == 0:
                if studentsPreferingZero == 0:
                    return studentsPreferingOne
                studentsPreferingZero -= 1
            else:
                if studentsPreferingOne == 0:
                    return studentsPreferingZero
                studentsPreferingOne -= 1

        return 0
