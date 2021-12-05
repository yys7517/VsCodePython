# 기존에 동일한 파일명이 있으면 새로운 내용으로 파일을 덮어쓴다.
file = open('test.txt','w')
file.write('Hello World!!\n파이썬 월드')
# file = open('test.txt','a')
# file.write('\n추가 Hello,World!!')
# 다음과 같은 내용을 추가해주는 것이 모드 a(append)이다.
file = open('test.txt','r')
read = file.read()
print( read )
file.close()


# x 모드
# file = open('test.txt','x')
# file.write('대한민국 만세!!')

# 파일이 존재하면 오류를 발생시키고, 파일이 존재하지 않으면 다음과 같은 파일을 만든다.


# with문을 사용하면 본문을 수행한 후 파일을 자동으로 닫아준다.

with open('test.txt','r') as file :
    read = file.read()
    print( read )



# csv 파일

import csv
listing = [ ['Malibu','Chevrolet',22965],
['Fusion','Ford',23735]
]

with open("car.csv","w",newline='') as f :
    car_writer = csv.writer(f)
    car_writer.writerows(listing)

with open("car.csv","r") as f :
    car_reader = csv.reader(f)
    for row in car_reader :
        names = row[0]
        makers = row[1]
        price = row[2]
        print( names,makers,price )