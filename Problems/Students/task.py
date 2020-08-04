class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = name[0][0]+last_name+birth_year

student = Student(input().split(), input(), input())
print(student.id)
