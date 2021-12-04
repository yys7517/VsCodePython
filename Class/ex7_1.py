class Registration:
    regi_num = 0        # 클래스변수

    def __init__(self,name) -> None:
        self.name = name        # 인스턴스변수
        Registration.regi_num += 1

    def __del__(self) :
        Registration.regi_num -= 1

student1 = Registration("홍길동")
student2 = Registration("김철수")

print(student1.name)
print(student2.name)
print(Registration.regi_num)
