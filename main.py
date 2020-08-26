import turtle
import random
import time


wn = turtle.Screen()
wn.title("my game")
wn.tracer(0)




def chooser():
    global choose
    choose = random.randint(int(1), int(9))
    print(choose)

chooser()


pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(0,-250)
pen.hideturtle()


one = turtle.Turtle()
one.penup()
one.goto(-255,244)
one.write("1",font=("arial",26,"normal"))
one.hideturtle()



two = turtle.Turtle()
two.penup()
two.goto(0,244)
two.write("2",font=("arial",26,"normal"))
two.hideturtle()

three = turtle.Turtle()
three.penup()
three.goto(255,244)
three.write("3",font=("arial",26,"normal"))
three.hideturtle()


four= turtle.Turtle()
four.penup()
four.goto(-255,-0)
four.write("4",font=("arial",26,"normal"))
four.hideturtle()

five = turtle.Turtle()
five.penup()
five.goto(0,0)
five.write("5",font=("arial",26,"normal"))
five.hideturtle()

six = turtle.Turtle()
six.penup()
six.goto(255,0)
six.write("6",font=("arial",26,"normal"))
six.hideturtle()

seven= turtle.Turtle()
seven.penup()
seven.goto(-255,-200)
seven.write("7",font=("arial",26,"normal"))
seven.hideturtle()

eight = turtle.Turtle()
eight.penup()
eight.goto(0,-200)
eight.write("8",font=("arial",26,"normal"))
eight.hideturtle()

nine= turtle.Turtle()
nine.penup()
nine.goto(255,-200)
nine.write("9",font=("arial",26,"normal"))
nine.hideturtle()



def one():
    if choose==1:
        pen.write("correct!",font=("arial",26,"normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def two():
    if choose==2:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def three():
    if choose==3:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def four():
    if choose==4:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def five():
    if choose==5:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def six():
    if choose==6:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def seven():
    if choose==7:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def eight():
    if choose==8:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


def nine():
    if choose==9:
        pen.write("correct!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()

    else:
        pen.write("wrong!", font=("arial", 26, "normal"))
        time.sleep(2)
        pen.clear()
        chooser()


wn.listen()
wn.onkeypress(one,"1")
wn.onkeypress(two,"2")
wn.onkeypress(three,"3")
wn.onkeypress(four,"4")
wn.onkeypress(five,"5")
wn.onkeypress(six,"6")
wn.onkeypress(seven,"7")
wn.onkeypress(eight,"8")
wn.onkeypress(nine,"9")

while True:
    wn.update()


wn.mainloop()
