def solution ( shirt_size ) :
    
    for i in shirt_size :
        if ( i == "XS" ) :
            orderlist.update({"XS" : orderlist.get(i)+1})
        elif ( i == "S" ) :
            orderlist.update({"S" : orderlist.get(i)+1})
        elif ( i == "M" ) :
            orderlist.update({"M" : orderlist.get(i)+1})
        elif ( i == "L" ) :
            orderlist.update({"L" : orderlist.get(i)+1})
        elif ( i == "XL" ) :
            orderlist.update({"XL" : orderlist.get(i)+1})
        elif ( i == "XXL" ) :
            orderlist.update({"XXL" : orderlist.get(i)+1})

    answer = [ orderlist.get("XS"),orderlist.get("S"),orderlist.get("M")
                ,orderlist.get("L"), orderlist.get("XL"),orderlist.get("XXL") ]

    return answer

orderlist = { "XS" : 0, "S" : 0, "M": 0, "L": 0 ,"XL" :0, "XXL" : 0 }
shirt_size = ["XS","S","L","L","XL","S"]
ret = solution( shirt_size )

print("Solution: return value of the function is", ret," .")

# 고객들이 주문한 셔츠를 사이즈 별로 몇 개인지 분류하라.