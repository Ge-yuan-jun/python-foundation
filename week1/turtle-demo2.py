#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 22:06:11 2019

@author: geyuanjun
"""

# https://fopp.umsi.education/runestone/static/fopp/PythonTurtle/AFewMoreturtleMethodsandObservations.html
# summary: https://fopp.umsi.education/runestone/static/fopp/PythonTurtle/SummaryOfTurtleMethods.html
import turtle
wn = turtle.Screen()
jose = turtle.Turtle()
jose.shape("turtle")
jose.penup()

for size in range(10):
    jose.forward()
    jose.stamp() # leave an impression on the canvas
    jose.forward(-50)
    jose.right(36)

wn.exitonclick()
