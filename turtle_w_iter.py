import turtle
import itertools
import time
import random

RED_LIGHT = turtle.Turtle()
GREEN_LIGHT = turtle.Turtle()
YELLOW_LIGHT = turtle.Turtle()
LIGHTS = 'red green yellow'.split()
FLASH = itertools.cycle(LIGHTS)
LIGHT_OUT = 'black'


class Color:
    def __init__(self):
        self.red_light = RED_LIGHT
        self.green_light = GREEN_LIGHT
        self.yellow_light = YELLOW_LIGHT

    def red(self, color):
        self.red_light.color(color)

    def yellow(self, color):
        self.yellow_light.color(color)

    def green(self, color):
        self.green_light.color(color)


class Shapes:
    def __init__(self):
        self.red_light = RED_LIGHT
        self.green_light = GREEN_LIGHT
        self.yellow_light = YELLOW_LIGHT

    def red_shape(self):
        self.red_light.shape('circle')
        self.red_light.shapesize(2, 2)
        self.red_light.penup()
        self.red_light.goto(0,47)

    def yellow_shape(self):
        self.yellow_light.shape('circle')
        self.yellow_light.shapesize(2, 2)
        self.yellow_light.penup()
        self.yellow_light.goto(0,0)

    def green_shape(self):
        self.green_light.shape('circle')
        self.green_light.shapesize(2, 2)
        self.green_light.penup()
        self.green_light.goto(0,-47)

    def rectangle(self):
        pen = turtle.Turtle()
        pen.begin_fill()
        pen.color('orange')
        pen.width(4)
        pen.hideturtle()
        pen.penup()
        pen.goto(-30, 70)
        pen.pendown()
        pen.fd(60)
        pen.rt(90)
        pen.fd(140)
        pen.rt(90)
        pen.fd(60)
        pen.rt(90)
        pen.fd(140)
        pen.end_fill()


def rg_timer():
    return random.randint(2, 5)


def light_rotation(flash):
    color = Color()
    for colors in flash:
        if colors == 'red':
            color.red(colors)
            color.yellow(LIGHT_OUT)
            time.sleep(rg_timer())
        elif colors == 'green':
            color.green(colors)
            color.red(LIGHT_OUT)
            time.sleep(rg_timer())
        else:
            color.yellow(colors)
            color.green(LIGHT_OUT)
            time.sleep(2)


def main():
    wn = turtle.Screen()
    wn.title('Stoplight by @Cphoto21')
    wn.bgcolor('black')

    shape = Shapes()
    shape.rectangle()
    shape.red_shape()
    shape.yellow_shape()
    shape.green_shape()

    light_rotation(FLASH)

    wn.mainloop()


if __name__ == '__main__':
    main()
