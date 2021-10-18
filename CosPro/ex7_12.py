import turtle
'''
def circle_area(radius):
    tmp = radius * radius * 3.141592
    return tmp

def circle_draw(radius):
    turtle.circle(radius)

r = int(input("반지름 : "))

turtle.setup(600, 500)
circle_draw(r)
tmpstr = "반지름" + str(r) + "인 원의 넓이 =" + str(circle_area(r))
turtle.write(tmpstr)

'''
def circle_area(radius):
    tmp = radius * radius * 3.141592
    return tmp

def circle_draw(radius):
    turtle.circle(radius)

r = int(input("반지름 : "))

turtle.setup(600, 500)
circle_draw(r)
tmpstr = "반지름" + str(r) + "인 원의 넓이 =" + str(circle_area(r))

turtle.up()         # 펜 들고
turtle.right(90)    # 꺾고
turtle.forward(15)  # 15만큼 가고
turtle.left(90)     # 다시 꺾고

# turtle.down()       # 다시 내리고.
# 그림 그리려면 내려야되는데, 
# 글씨 쓰는거라 안 내려도됨. 

turtle.write(tmpstr)