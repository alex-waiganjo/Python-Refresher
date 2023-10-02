# Polymorphism

class Student:
    def __init__(self, name, age, course, gender) -> None:
        self.name = name
        self.age = age
        self.course = course
        self.gender = gender

    def info(self):
        return f"{self.name} is {self.age} years old pursuing {self.course}"


class Lecturer:
    def __init__(self, name, age, course, gender) -> None:
        self.name = name
        self.age = age
        self.course = course
        self.gender = gender

    def details(self):
        return f'{self.name} is {self.age} years old teaching {self.course}'


student_1 = Student("Alex", 40, "IT", "Male")
lec_1 = Lecturer("Jane", 42, "Computer Science", "Female")
print(student_1.info())
print(lec_1.details())
