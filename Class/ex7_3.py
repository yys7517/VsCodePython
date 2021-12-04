genel = 15

class Solar :
    def __init__(self,city,sunny) -> None:
        self.city = city
        self.sunny = sunny

    def print_city(self) : 
        print(f"{self.city}의 일조시간 : {self.sunny} hours")
        output = self.sunny * genel / 1000
        print(f"{self.city}의 발전량 : {output} kWh\n")

seoul = Solar("서울",1865)
jeju = Solar("제주",1767)

seoul.print_city()
jeju.print_city()
