class Calc:
    def __init__(self,first,second) -> None:
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def mul(self) :
        return self.first * self.second
    def sub(self) :
        return self.first - self.second
    def div(self) :
        return self.first / self.second

class InheritCalc(Calc) :   # InheritCalc 클래스는 Calc 클래스를 상속받음
    # 상속받은 add,mul,sub,div는 그대로 사용하고
    # first와 second 또한 상속받아 사용
    # trpl 메서드까지 선언하고 사용한다.
    def trpl(self):
        return self.first ** self.second

class SafeDivCalc(Calc):
    def div(self):              # 부모인 Calc의 div 메서드를 재정의.( 메서드 오버라이딩 )
        if self.second == 0 :   # 나누는 수가 0인 경우 0을 리턴하도록 수정.
            return 0
        else : 
            return self.first / self.second


Calc1 = Calc(4,2)
print( Calc1.add() )
print( Calc1.div() )

Calc2 = InheritCalc(6,2)
print ( Calc2.add() )
print ( Calc2.div() )



