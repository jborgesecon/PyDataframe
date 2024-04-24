import random as rd
import pandas as pd
import time 
import numpy as np


def intValid(text):
    while True:
        try:
            num = int(input(text))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return num

