import random as rd
print( rd.random() )     # 0이상 1미만의 난수(실수) 발생.
print( rd.randint(1,6) ) # 1이상 6이하의 정수를 발생.
print( rd.randrange(1,6) ) # 1이상 6미만의 정수를 발생.
numlist = [10,20,30,40,50]
rd.shuffle(numlist)
print(numlist)
print(rd.choice(numlist))       # numlist의 원소중에서 임의로 하나를 고른다.
print(rd.sample(numlist,3))     # numlist의 원소중에서 임의로 3개를 고른다.
print('-'*50)

import sys
print(sys.path)
print('-'*50)
print(sys.prefix)
print('-'*50)
print(sys.copyright)
print('-'*50)
print(sys.getwindowsversion())

import calendar

print(calendar.monthrange(2020,12))
print('-'*20)
print(calendar.weekday(2020,8,31))  # 월요일 0 ~ 일요일 6
print('-'*20)
print(calendar.prmonth(2021,8))
print('-'*20)
print(calendar.prmonth(2021,12))


print('-'*20)

text = '파이썬 프로그래밍!!'
with open('python.txt','w') as p:
    p.write(text)
    # write 함수 매개변수에는 string형만 전달되어야 한다.
import pickle

list = ['a','b','c']
with open('list.txt','wb') as f:
    pickle.dump(list,f)
    
with open('list.txt','rb') as f :
    data = pickle.load(f)

print(data)

