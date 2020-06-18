students = []
score_list = []

for _ in range(int(input())):

    temp = []

    name = input()
    score = input()

    temp.append(name)
    temp.append(float(score))

    score_list.append(float(score))
    students.append(temp)#Nested List

score_list = list(dict.fromkeys(score_list))
score_list.sort()
print(students)
if len(students)>=2:
    student_low = []
    score_low = [score_list[1]]

    for i in students:
        if score_low == i:
            student_low.append(i[0])
        else:
            continue
    print()
else:
    students[0][0]
