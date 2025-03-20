# 빵 클래스 정의
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
            print("구매해주셔서 감사합니다.")
            self.stock -= 1
            return True

# 빵 클래스를 상속받아 붕어빵 클래스 정의
class FishShapedBun(Bread):
    def __init__(self, name, price, stock, inside):
        super().__init__(name, price, stock)
        self.inside = inside

    def buy(self):
        if super().buy():  # 부모 클래스의 buy() 실행 후 성공하면 추가 메시지 출력
            print(f'맛있는 {self.inside} 붕어빵!')

# 붕어빵 객체 생성 및 테스트
fish_shaped_bun = FishShapedBun("붕어빵", 1000, 10, "팥")

for i in range(11):  # 11번 구매 시도 (10개 재고이므로 마지막 시도에서 "재고가 없습니다." 출력됨)
    fish_shaped_bun.buy()
