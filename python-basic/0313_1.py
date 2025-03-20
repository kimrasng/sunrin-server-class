# 파이썬 자료형 확인하기
num_i = 45
num_f = 20.54
str_n = "김도현"
list_n = [1, 2, 3]
dict_n={"name": "김도현"}

# print((type(num_i)))
# print((type(num_f)))
# print((type(str_n)))
# print((type(list_n)))
# print((type(dict_n)))

# 클래스 만들기
class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("----- 학생 목록 -----")
        print("이름\t국어\t수학\t영어\t총점")
        for student in cls.students:
            print(student.to_string())

    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english

    def to_string(self):
        return f'{self.name}\t{self.korean}\t{self.math}\t{self.english}\t{self.get_sum()}'

student1 = Student("김도현", 99, 88, 77)
student2 = Student("A", 29, 58, 67)
student3 = Student("B", 39, 48, 27)

# print(students.to_string())
# print(students.get_sum())
# Student.print()

# 연습문제
class users:
    def __init__(self, name, number, major):
        self.name = name
        self.number = number
        self.major = major

    def to_string(self):
        return f'{self.name}\t{self.number}\t{self.major}'

    def get_name(self):
        return self.name


# users = users("김도현", 20502, "SW")
# print(users.to_string())
# print(users.get_name())

# 연습문제

class weather:
    count = 0
    weathers = []

    @classmethod
    def print(cls):
        print("----- 날씨 목록 -----")
        print("날짜\t날씨\t온도")
        for weather in cls.weathers:
            print(weather.to_string())

    def __init__ (self, time, wind, temperature):
        self.day = time
        self.weather = wind
        self.temperature = temperature

        weather.count += 1
        weather.weathers.append(self)

    def to_string(self):
        return f'{self.day}\t{self.weather}\t{self.temperature}'

weather1 = weather("02:10", "맑음", -3)
weather2 = weather("05:20", "흐림", 4)
weather3 = weather("08:30", "비", 10)

weather.print()

