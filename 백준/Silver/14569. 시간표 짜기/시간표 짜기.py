N = int(input())
courses = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    courses.append(set(tmp[1:]))

M = int(input())
students = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    students.append(set(tmp[1:]))

for student in students:
    count = 0
    for course in courses:
        if course.intersection(student) == course:
            count += 1
    print(count)