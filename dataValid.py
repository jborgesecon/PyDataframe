import random as rd
import pandas as pd
import time 
import numpy as np


def sepper(msg, sep):
    print('\n', msg.center(30, sep))

def header(msg):
    print('\n')
    print(30 * '=')
    print(msg.center(30))
    print(30 * '=', '\n')

def intValid(num):
    while True:
        try:
            num = int(num)
            break
        except:
            print("Please enter a valid number")
            num = input("Enter a number: ")
    return num
