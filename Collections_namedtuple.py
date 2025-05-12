from collections import namedtuple

num_students = int(input())

Student = namedtuple('Student', input())

data_list = [input().split() for i in range(num_students)]

a = (sum([int(Student(data[0], data[1], data[2], data[3]).MARKS) for data in data_list])/num_students)

print(f'{a:.2f}')