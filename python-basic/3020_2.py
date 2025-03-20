# 예외처리
try:
    num = int(input("숫자 입력 : "))
    raise IndexError()
except Exception as exception:
    print("입력은 숫자로만 이루어져야합니다.")
    print(f"{exception}, {type(exception)}")
else:
    print(f'{num}의 제곱은 {num**2}입니다.')
finally:
    print("프로그램 종료")
