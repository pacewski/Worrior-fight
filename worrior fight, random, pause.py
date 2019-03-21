# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:28:25 2019

@author: pacew
"""
import random
import time

'''
def Hello():
    name = input("what is your name? \n")
    country = input("what country are you from? \n")
    print("Hello {} from {}".format(name, country))
'''

'''
Creating a class of worrior,
Worriors are going to fight between
attack with change i.e 10= 10% to hit
if hit, takes lifes equals to strengh.
When health goes to 0- dies
'''


class Worrior:
    def __init__(self, name, strengh=2, chance=30, health=10, status="alive"):
        self.name = name
        self.strengh = strengh
        self.chance = chance
        self.health = health
        self.status = status

    def attack(self):
        print(self.name + " is trying to hit oponent")
        hitChanceRandom = random.randint(0, 100)
        if self.chance >= hitChanceRandom:
            hit = True
            print("it is a hit from " + self.name + "\n")
        else:
            hit = False
            print(self.name + " missed \n")
        return hit


def createWorrior():
    global worrior1
    nameWorrior = input("Name your worrior: \n")
    worrior1 = Worrior(nameWorrior)
    print(worrior1.name + " is ready to fight")
    print(worrior1.strengh)
    return worrior1


def createOpponentWorrior():
    global worrior2
    nameWorrior = input("Name your opponent worrior: \n")
    worrior2 = Worrior(nameWorrior)
    print(worrior2.name + " is ready to fight")
    print(worrior2.strengh)


def fight(x, y):
    print(x.name + " and " + y.name + " are going to fight till death!")
    time.sleep(2)
    i = 0
    while 0 == 0:
        i = i + 1
        x.attack()
        if x.attack() is True:
            y.health = y.health - x.strengh
            print(y.name, " has ", y.health, " HP left")
            time.sleep(2)
        if y.health <= 0:
            y.status = "dead"
            print("Battle is over! ", x.name, " has won!")
            break

        y.attack()
        if y.attack() is True:
            x.health = x.health - y.strengh
            print(x.name, " has ", x.health, " HP left")
            time.sleep(2)
        elif x.health <= 0:
            x.status = "dead"
            print("Battle is over! ", y.name, " has won!")
            break
    print("this round has taken ", i, "turns")
    print(x.name, " has ", x.health, " HP and is ", x.status)
    print(y.name, " has ", y.health, " HP and is ", y.status)


createWorrior()
createOpponentWorrior()
fight(worrior1, worrior2)

