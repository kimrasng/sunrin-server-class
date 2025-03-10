# 함수 결과 반환
def compare_num(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

# print(compare_num(0))

# 도전문제
def up_down(n, num):
    if n > num:
        return "Down"
    elif n < num:
        return "Up"
    return "정답 입니다!"

def game ():
    import random
    num = random.randint(1, 100)
    while True:
        print("=====================================")
        n = int(input("숫자를 입력하세요: "))
        result = up_down(n, num)
        print(result)
        if result == "정답 입니다!":
            break

# game()


# 매개 변수를 함수로 받아서 실행
def call_10_times(func):
    for i in range(10):
        func()

def say_love():
    print("I love python")

# call_10_times(say_love)


# map(), filter() 함수 활용
def super(num):
    return num * num

def is_big_10(num):
    return num > 10

num_list = [30, 20, 50, 14, 8, 26]

output_map = map(super, num_list)
print("map:", list(output_map))

output_filter = filter(is_big_10, num_list)