# 백준 브론즈5 - 검증수.
list = []
list = input().split()

sum = 0
for i in list :
    sum += int(i) ** 2

print ( sum % 10 )