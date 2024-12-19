
n = int(input("Enter the number of students who play cricket: "))
cricket = []
for i in range(n):
    roll_no = int(input("Enter the roll number of student: "))
    cricket.append(roll_no)
print("The set of students who play cricket:", cricket)

n2 = int(input("Enter the number of students who play badminton: "))
badminton = []
for i in range(n2):
    roll_no = int(input("Enter the roll number of the student: "))
    badminton.append(roll_no)
print("The set of students who play badminton:", badminton)

n3 = int(input("Enter the number of students who play football: "))
football = []
for i in range(n3):
    roll_no = int(input("Enter the roll number of the student: "))
    football.append(roll_no)
print("The set of students who play football:", football)


def intersection(l1, l2):
    res = []
    for i in l1:
        if i in l2 and i not in res:
            res.append(i)
    return res


    res = l1[:]
    for i in l2:
        if i not in res:
            res.append(i)
    return res


def diff(l1, l2):
    res = []
    for i in l1:
        if i not in l2:
            res.append(i)
    return res


students_cricket_and_badminton = intersection(cricket, badminton)
print("List of students who play both cricket and badminton:", students_cricket_and_badminton)


students_either_cricket_or_badminton = diff(cricket, badminton) + diff(badminton, cricket)
print("List of students who play either cricket or badminton but not both:", students_either_cricket_or_badminton)


all_students = cricket[:]
for i in badminton:
    if i not in all_students:
        all_students.append(i)
for i in football:
    if i not in all_students:
        all_students.append(i)
students_neither_cricket_nor_badminton = diff(all_students, union(cricket, badminton))
print("Number of students who play neither cricket nor badminton:", len(students_neither_cricket_nor_badminton))

# d) Number of students who play cricket and football but not badminton
students_cricket_and_football = intersection(cricket, football)
students_cricket_football_not_badminton = diff(students_cricket_and_football, badminton)
print("Number of students who play cricket and football but not badminton:", len(students_cricket_football_not_badminton))
