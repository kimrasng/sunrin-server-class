# 정삼각형 클래스 만들기

class ETriangle:
    def __init__(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_length(self, length):
        if length <= 0:
            print("길이는 양수로 설정해주세요.")
            return
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if length <= 0:
            raise ValueError("길이는 양수이여야 합니다.")
        self.__length = length

# 정삼각형 클래스 사용해보기
# triangular = ETriangle(5)
#
# triangular.__length = 3
# # print(triangular.__length)
# print(triangular.get_length())
# triangular.set_length(3)
# triangular.set_length(-3)
# print(triangular.get_length())
#
# print("=================--")
# triangular.length = 9
# print(triangular.length)
# triangular.length = -9
#

# 연슴

class wallet:
    def __init__(self, money):
        self.__money = money

    def get_money(self):
        return self.__money

    def set_money(self, money):
        if money < 0:
            print("돈은 양수로 설정해주세요.")
            return
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if money < 0:
            raise ValueError("돈은 양수이여야 합니다.")
        self.__money = money

wallet1 = wallet(1000)
print(wallet1.get_money())
wallet1.set_money(2000)
wallet1.set_money(-2000)
print(wallet1.get_money())