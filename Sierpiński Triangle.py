# based off No Strach Press book
import turtle
turtle.tracer(100,0)
turtle.setworldcoordinates(0,0,700,700)
turtle.hideturtle()

MIN_SIZE = 4

def midpoint(startx, starty, endx, endy):
    xDiff = abs(startx - endx)
    yDiff = abs(starty - endy)
    return (min(startx, endx) + (xDiff / 2.0), min(starty, endy) + (yDiff/ 2.0))

def isTooSmall(ax, ay, bx, by, cx, cy):
    width = max(ax, bx, cx) - min(ax, bx, cx)
    height = max(ay, by, cy) - min(ay, by, cy)
    return width < MIN_SIZE or height < MIN_SIZE

def drawTriangle(ax, ay, bx, by, cx, cy):
    if isTooSmall(ax, ay, bx, by, cx, cy):
        return
    else:
        turtle.penup()
        turtle.goto(ax, ay)
        turtle.pendown()
        turtle.goto(bx, by)
        turtle.goto(cx, cy)
        turtle.goto(ax, ay)
        turtle.penup()

        mid_ab = midpoint(ax, ay, bx, by)
        mid_bc = midpoint(bx, by, cx, cy)
        mid_ca = midpoint(cx, cy, ax, ay)

        drawTriangle(ax, ay, mid_ab[0], mid_ab[1], mid_ca[0], mid_ca[1])
        drawTriangle(mid_ab[0], mid_ab[1], bx, by, mid_bc[0], mid_bc[1])
        drawTriangle(mid_ca[0], mid_ca[1], mid_bc[0], mid_bc[1], cx, cy)
        return
# Equilaterial Sierpinski Triangle
drawTriangle(50,50,350,650,650,50)

# Skewed Sierpinski Triangle
# drawTriangle(30,250,680,600,500,80)
turtle.exitonclick()