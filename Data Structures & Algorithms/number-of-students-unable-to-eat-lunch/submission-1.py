class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count, n = 0, len(students)
        while count < len(students):
            if students[0] != sandwiches[0]:
                count += 1
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)
                count = 0
        
        return count