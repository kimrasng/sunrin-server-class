# 상송 사용하기
# 빵 클래스 만들어보기
class Bread:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self):
        if self.stock <= 0:
            print("재고가 없습니다.")
            return
        else:
            print("구매해주세서 감사합니다.")
            self.stock -= 1

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self):
        if self.stock <= 0:
            print("재고가 없습니다.")
            return False
        else:
            print("구매해주셔서 감사합니다.")
            self.stock -= 1
            return True

    def bake(self, stock):
        return


# 빵 클래스를 상속받아 붕어빵 클래스 만들기
class FishShapedBun(Bread):
    def __init__(self, name, price, stock, inside):
        super().__init__(name, price, stock)
        self.inside = inside

    def buy(self):
        if super().buy():
            print(f'맛있는 {self.inside} 붕어빵!')

fish_shaped_bun = FishShapedBun("붕어빵", 1000, 10, "팥")
for i in range(11):
    fish_shaped_bun.buy()# 빵 클래스 정의
class Bread:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self):
        if self.stock <= 0:
            print("재고가 없습니다.")
            return False
        else:
            print(f"{self.name}을(를) 구매해주셔서 감사합니다.")
            self.stock -= 1
            return True

    def bake(self, quantity):
        self.stock += quantity
        print(f"{self.name}이(가) {quantity}개 더 만들어졌습니다. 현재 재고: {self.stock}")

# 빵 클래스를 상속받아 붕어빵 클래스 만들기
class FishShapedBun(Bread):
    def __init__(self, name, price, stock, inside):
        super().__init__(name, price, stock)
        self.inside = inside  # 올바르게 수정

    def buy(self):
        if super().buy():
            print(f"맛있는 {self.inside} 붕어빵을 즐기세요!")

# 빵 객체 생성 및 테스트
bread = Bread("식빵", 3000, 10)
for i in range(11):
    bread.buy()

print("\n")

# 붕어빵 객체 생성 및 테스트
fish_shaped_bun = FishShapedBun("붕어빵", 1000, 10, "팥")
for i in range(11):
    fish_shaped_bun.buy()

print("\n")

# 붕어빵 추가 생산 후 다시 구매
fish_shaped_bun.bake(10)
for i in range(10):
    fish_shaped_bun.buy()

# isinstance 테스트
print(isinstance(bread, Bread))  # True
print(isinstance(bread, FishShapedBun))  # False
print(isinstance(fish_shaped_bun, Bread))  # True

bread = Bread("식빵", 3000, 10)
for i in range(11):
    bread.buy()


# 빵클래스 상속받아 붕어빵 클래스 만들기

class FishShapedBun(Bread):
    def __init__(self, name, price, stock, inside):
       super().__init__(name, price, stock)
       slice.inside = inside


    def buy(self):
        super().buy()
        print(f'맛있는 {self.inside}붕어빵')

# fish_shaped_bun = FishShapedBun("붕어빵", 1000, 10, "팥")
for i in range(11):
    fish_shaped_bun.buy()

fish_shaped_bun.bake(10)

for i in range(10):
    fish_shaped_bun.buy()


print(isinstance(bread, Bread))
print(isinstance(bread, FishShapedBun))
print(isinstance(fish_shaped_bun, Bread))

print("===================")
print(type(bread) == Bread)
print(type(bread) == FishShapedBun)
print(type(fish_shaped_bun) == Bread)
print(type(fish_shaped_bun) == FishShapedBun)





# 연슴문제

class Weather:
    count = 0
    weathers = []

    @classmethod
    def print(cls):
        print("----- 날씨 목록 -----")
        print("날짜\t날씨\t온도")
        for weather in cls.weathers:
            print(weather.to_string())

    def __init__(self, time, wind, temperature):
        self.day = time
        self.weather = wind
        self.temperature = temperature

        Weather.count += 1
        Weather.weathers.append(self)

    def to_string(self):
        return f"{self.day}\t{self.weather}\t{self.temperature}°C"

class DetailedWeather(Weather):
    def __init__(self, time, wind, temperature, humidity):
        super().__init__(time, wind, temperature)
        self.humidity = humidity  # 추가 속성 (습도)

    def to_string(self):
        return f"{self.day}\t{self.weather}\t{self.temperature}°C\t습도: {self.humidity}%"

    @classmethod
    def print(cls):
        print("===== 상세 날씨 목록 =====")
        print("날짜\t날씨\t온도\t습도")
        for weather in cls.weathers:
            print(weather.to_string())

weather1 = Weather("02:10", "맑음", -3)
weather2 = Weather("05:20", "흐림", 4)

weather3 = DetailedWeather("08:30", "비", 10, 85)
weather4 = DetailedWeather("12:45", "눈", -5, 90)

print("✅ 부모 클래스 출력:")
Weather.print()

print("\n✅ 자식 클래스 출력:")
DetailedWeather.print()