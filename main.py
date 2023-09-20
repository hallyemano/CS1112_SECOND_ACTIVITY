student_name = input("Student name:")
ID = input("ID:")
course_section = input("Course and Section:")
G1 = eval(input("First Quarter Grade:"))
G2 = eval(input("Second Quarter Grade:"))
G3 = eval(input("Third Quarter Grade:"))
G4 = eval(input("Fourth Quarter Grade:"))

ave = (G1 + G2 + G3 + G4) / 4

print(student_name)
print(ID)
print(course_section)
print(G1)
print(G2)
print(G3)
print(G4)
print(ave)

