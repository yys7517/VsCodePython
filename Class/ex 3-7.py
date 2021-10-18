birth = int(input('생년월일을 입력하세요 : '))
year = birth // 10000
month1 = birth % 10000 // 100
month2 = birth // 100 % 100
date = birth % 100
print(year,month1,month2)
print("생년월일 : {}년 {}월 {}일".format(year,month1,date))