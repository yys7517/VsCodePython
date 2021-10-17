# 백준 브론즈4 - TV크기
# 대각선의 길이, 높이 비율, 너비 비율
len,h,w = input().split()
len = int(len)
h = int(h)
w = int(w)

# 대각선 비율 rate
rate = ( h ** 2 + w ** 2 ) ** (1/2)
# print (rate)

# 비율 1에 대한 길이 = int( len / rate )
print(  int( h * ( len / rate ) ) ,end=' ')
print(  int( w * ( len / rate ) ) ,end=' ')
