# 함수 만들기

def say_hello_5times():
    for i in range(5):
        print("Hello")


def say_hello_n_times(n, str):
    for i in range(n):
        print(str)

# say_hello_n_times(10, "안녕하세요")
# say_hello_5times()

# 가변 매개변수
def say_string_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

# say_string_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")


# 기본 매개변수
def say_strings_d_times(*values, d=3):
    for i in range(d):
        for value in values:
            print(value)
        print()

# say_strings_d_times("안녕하세요", "쿼티입니다", d=3)

# 연습 문제

def function_ex1(*values, num=0):
    print("num:", num)
    print("values:", values)
    for value in values:
        print(value)

def function_ex2(num=0, *values):
    print("num:", num)
    print("values:", values)
    for value in values:
        print(value)


function_ex1("선린", "솦과", num=1)
# function_ex2("선린", "솦과", 1)

