import turtle
import random
import pygame

a = turtle.Turtle()

b = input('Сколько игроков бет играть? ')

if b > '2':
    print('Слишком много игроков! Максимум 2 игрока!')
elif b <= '1':
    print('Слишком мал+о игроков! Нужно мининум 2 игрока! ')
else:
    print('Отлично!')
    d = input('Введите ник первого игрока: ')
    d1 = input('Введите ник второго игрока: ')
    

for i in range(1):
    b = random.uniform(1,6)
    c = round(b)

a.speed(9999)

if c == 1: 
   for n in range(4):
       a.fd(160)
       a.rt(90)
   a.penup()
   a.goto(80,-100)
   a.pendown()
   a.circle(20)


if c == 2:
   for u in range(4):
       a.fd(160)
       a.rt(90)
   a.penup()
   a.goto(40,-140)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(120,-60)
   a.pendown()
   a.circle(20)

if c == 3:
   for h in range(4):
       a.fd(160)
       a.rt(90)
   a.penup()
   a.goto(40,-140)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(80,-100)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(120,-60)
   a.pendown()
   a.circle(20)

if c == 4:
   for p in range(4):
       a.fd(160)
       a.rt(90)
   a.penup()
   a.goto(40,-60)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(120,-60)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(40,-140)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(120,-140)
   a.pendown()
   a.circle(20)

if c == 5:
   for lo in range(4):
       a.fd(160)
       a.rt(90)
   a.penup()
   a.goto(40,-60)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(120,-60)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(40,-140)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(120,-140)
   a.pendown()
   a.circle(20)
   a.penup()
   a.goto(80,-100)
   a.pendown()
   a.circle(20)

if c == 6:
   for oi in range(4):
       a.fd(160)
       a.rt(90)
   a.penup()
   a.goto(40,-140)
   a.pendown()
   a.circle(15)
   a.penup()
   a.goto(40,-95)
   a.pendown()
   a.circle(15)
   a.penup()
   a.goto(40,-50)
   a.pendown()
   a.circle(15)
   a.penup()
   a.goto(120,-140)
   a.pendown()
   a.circle(15)
   a.penup()
   a.goto(120,-95)
   a.pendown()
   a.circle(15)
   a.penup()
   a.goto(120,-50)
   a.pendown()
   a.circle(15)    



