def solution( value, unit ) :
    if unit == "C" :
        value = (value*1.8) + 32
    if unit == "F" :
        value = (value-32) / 1.8

    return int(value)


value = 527
unit = "F"
ret = solution( value, unit )
print ("solution 함수의 반환 값은", ret, "입니다.")