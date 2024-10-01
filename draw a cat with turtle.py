from turtle import *
def draw_cat():
    speed(13) # Painting speed control
    bgcolor("orange") #choose the background color
    pensize(10) #Define the pensize
    penup()
    goto(0, 100) #Move the pen to the target pixel
    pendown()


    seth(0)
    fd(60)
    seth(60)
    fd(75)

    seth(-80)
    fd(150)
    seth(30)
    fd(50)
    seth(-150)
    fd(50)
    seth(0)
    fd(50)
    seth(-180)
    fd(50)
    seth(-30)
    fd(50)
    seth(150)
    fd(50)
    seth(-80)
    fd(150)

    seth(180)
    fd(300)

    seth(80)

    fd(150)
    seth(-150)
    fd(50)
    seth(30)
    fd(50)
    seth(-180)
    fd(50)
    seth(0)
    fd(50)
    seth(150)
    fd(50)
    seth(-30)
    fd(50)
    seth(80)
    fd(150)

    seth(-60)
    fd(75)
    seth(0)
    fd(60)
    end_fill()
    penup()
    goto(-50, 0)  # Move the pen to the target pixel
    pendown()
    color("black", "white")
    begin_fill()
    circle(25)
    end_fill()
    color("black", "black")
    begin_fill()
    circle(10)
    pendown()
    end_fill()

    penup()
    goto(50, 0)  # Move the pen to the target pixel
    pendown()
    color("black", "white")
    begin_fill()
    circle(25)
    end_fill()
    color("black", "black")
    begin_fill()
    circle(10)
    pendown()
    end_fill()

    penup()
    goto(0, -50)
    pendown()
    seth(-90)
    circle(30, 150)
    penup()
    goto(0, -50)
    pendown()
    seth(-90)
    circle(-30, 150)
    exitonclick()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    draw_cat()

