import calendar as c
def solution(weekday) :
    if weekday == 0 :
        return 'MON'
    elif weekday == 1 :
        return 'TUE'
    elif weekday == 2 :
        return 'WED'
    elif weekday == 3 :
        return 'THU'
    elif weekday == 4 :
        return 'FRI'
    elif weekday == 5 :
        return 'SAT'
    else :
        return 'SUN'
        
x,y = map(int, input().split() )
weekday = c.weekday(2007,x,y)
result = solution(weekday)
print(result)
