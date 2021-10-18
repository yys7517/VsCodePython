# fc(temper,action)
# action = 1 이면 화씨 -> 섭씨
# action = 0 이면 섭씨 -> 화씨
def fc(temper,action) :
    if action == 0 :
        tmp = temper * 1.8 + 32
        tmpact = "C2F"

    else :
        tmp = ( temper -  32 ) / 1.8
        tmpact = "F2C" 
    return (tmp,tmpact) 

temper = int(input("온도 : "))
action = int(input("변환(0:C2F, 1:F2C) : "))
(rt,ra) = fc(temper,action)
print(ra, ":", temper, "=>", rt)
