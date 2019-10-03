# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

if __name__ == '__main__':
    total_students = int(input())
    data_format = namedtuple('Student', list(map(str, input().split())))
    marks = 0

    for _ in range(total_students):
        student_data = tuple(map(str, input().split()))
        student = data_format(*student_data)
        marks += int(student.MARKS)

    print("%.2f" % float(marks/total_students))
