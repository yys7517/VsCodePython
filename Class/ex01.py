# import keyword
# print(keyword.kwlist)

# no = None
# print(no)
# print(type(no))

# 부울형 (boolean, bool)
# True, False (소문자 주의)

# b1 = True
# print(type(b1), b1)
# <class 'bool'> True 

# b2 = False
# print(type(b2), b2)
# <class 'bool'> False

# true = True
# b3 = true 
# print( type(b3),b3)
# NameError: name 'true' is not defined

# a = 1.2
# b = -3.45
# print(a,type(a))
# print(b,type(b))
# c = 4.24E10
# d = 4.24e-2
# print(c)
# print(d)

# e = 2-3j
# print(e.real)
# print(e.imag)
# print(type(e))

# str1 = "작은따옴표의 모양은 ' 이다"
# str2 = '큰따옴표의 모양은 " 이다'
# print(str1)
# print(str2)

# str3 = "큰따옴표의 모양은 \" 이다"
# print(str3)

# print('|%10s|' % '컴퓨터공학') # 오른쪽정렬
# print('|%-10s|' % '컴퓨터공학') # 왼쪽정렬

# print('|%10.5f|' % 3.1415926 )
# print('|%-10.5f|' % 3.1415926 )
# print('|%0.5f|' % 3.1415926)
# print('|%0.5f|' % 123.1415926 )

# str11 = 'Department of {}'
# print(str11.format('Computer'))
# str12 = 'Department of {} {}'
# print(str12.format('Computer','Engineering'))
# str13 = 'hello, {0} {1}'
# str13 = 'hello, {1} {0}'
# print(str13.format("Computer","Engineering"))

str14 = "hello, {str1}{str2}"
print(str14.format(str1="컴퓨터",str2="공학과"))

str15 = "Department of {:20}"
print(str15.format("Engineering") + "/")

str15 = "Department of {:<20}"
print(str15.format("Engineering") + "/")
# 왼쪽 정렬

str15 = "Department of {:>20}"
print(str15.format("Engineering") + "/")
#오른쪽 정렬

str15 = "Department of {:^20}"
print(str15.format("Engineering") + "/")
#가운데 정렬

# 차지하는 공간을 다른 문자열로 채우기

str15 = "Department of {:@<20}"
print(str15.format("Engineering") + "/")
str15 = "Department of {:#>20}"
print(str15.format("Engineering") + "/")
str15 = "Department of {:$^20}"
print(str15.format("Engineering") + "/")