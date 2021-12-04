class Student:
    # def __init__(self,name) :
    #     self.name = name

    def __init__(self,name,email,phone) :
        self.name = name
        self.email = email
        self.phone = phone

    def to_print(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.email,
            self.phone)

    def __del__(self) :
        print(self.name, "객체가 소멸되었습니다.")

    def __repr__(self) -> str:
        return self.name
        # 인스턴스를 호출할 때 문자열을 반환하는 __repr__메서드

students = [
    Student("홍길동","hong1234@email.net","010-1234-5678"),
    Student("김철수","kim1234@email.net","010-2345-6789")
]

for student in students :
    print( student.to_print() )
   
# del [인스턴스명]
# del 키워드를 사용하여 인스턴스를 삭제할 수 있다.

# student1 = Student("홍길동")
# student2 = Student("김철수")
# student3 = Student()

# 생성자가 name 매개변수를 포함하고 있는 생성자만 있으므로
# 에러가 난다. name 매개변수 값에 값을 넣어줘야 한다.

# print( student1.name )
# print( student2.name )

# print( student3.name )
