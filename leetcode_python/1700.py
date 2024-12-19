class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        students1 = sum(students)
        students0 = len(students) - students1
        no_of_sandwich0 = 0
        no_of_sandwich1 = 0
        for sandwich in sandwiches:
            if sandwich == 1:
                no_of_sandwich1 += 1
            else:
                no_of_sandwich0 += 1
            if no_of_sandwich1 > students1 or no_of_sandwich0 > students0:
                # +1 cause feed one extra then breaking
                return len(sandwiches) - no_of_sandwich0 - no_of_sandwich1 + 1 
        return 0
# implement stack queue solution too
