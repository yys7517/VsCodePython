# 정확하게 24시간이 될 때 잡으려고 한다.

now =input().split(':')
start = input().split(':')


Time = []
Time.append( int(now[0]) * 3600 + int(now[1]) * 60 + int(now[2]) * 1 )
Time.append( int(start[0]) * 3600 + int(start[1]) * 60 + int(start[2]) * 1 )
# Time[1] 시작시간 초 변환
# Time[0] 현재시간 초 변환
diff = Time[1] - Time[0]

if diff < 0 :    # 현재 시간이 더 클 때, now = 14:30:30, start = 14:00:00                           
    diff += 60 * 60 * 24
    # 임무를 시작한지 30분 30초밖에 안지남. 
    # diff에는 30분 30초의 값이 음수로 들어가있음. 23시간 29분 30초가 남았음을 보여주기 위해
    # diff 에 24시간의 값을 더해준다.

h = diff // 3600                    # 3600 초 = 1 시간
m = ( diff % 3600 ) // 60           # 
s = diff % 60
print("%02d:%02d:%02d" % (h,m,s))
