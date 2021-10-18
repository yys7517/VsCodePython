import turtle
def draw_rectangle(x,y) :
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)
    turtle.right(90)
    turtle.forward(x)
    turtle.right(90)
    turtle.forward(y)

def rectangle_area(x,y) :
    return x*y


x = int(input("가로 : "))
y = int(input("세로 : "))
turtle.setup(600,400)
draw_rectangle(x,y)
tmpstr = "가로" + str(x) + "세로" + str(y) + "인 사각형의 넓이 = " + str(rectangle_area(x,y))
turtle.write(tmpstr)