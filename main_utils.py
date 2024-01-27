#this file will contain the main Functions I will call on all the other .py documents

import random as rd
import unicodedata
error = ('type a valid answer: ')
yes_or_no = ('type "y" for YES and "n" for NO: ')
n_or_p = 'type "n" for NEXT and "p" for PREVIOUS: '

#Input Validation

def strvalid(text):
    while True:
        try:
            m1 = str(text).strip()
            break
        except ValueError:
            text = input(error)
    return m1
        
def intvalid(text):
    while True:
        try:
            m2 = int(text)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            text = input(error)
    return m2

def floatvalid(text):
    while True:
        try:
            m2 = float(text)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            text = input(error)
    return m2

def isprime(text):
    t01 = 0
    for i in range(1, text+1):
        if text % i == 0:
            t01 += 1
    # if t01 > 2:
    #     m03 = ('FALSE')
    # elif t01 == 2:
    #     m03 = ('TRUE')
    # else:
    #     m03 = t01
    
    # m03 = t01 > 2 ? ('FALSE') : t01 == 2 ? ('TRUE') : t01

    m03 = False if t01 > 2  else True if t01 == 2 else t01
    
    return m03

def iseven(text):
    m8 = text % 2
    if m8 == 0:
        m81 = True
    else:
        m81 =False
    return m81

def ynvalid(text):
    while True:
        m04 = text.lower().strip()
        if m04 == 'y' or m04 == 'n':
            break
        else:
            text = input(yes_or_no)
    return m04

def npvalid(text):
    while True:
        m04 = text.lower().strip()
        if m04 == 'n' or m04 == 'p':
            break
        else:
            text = input(n_or_p)
    return m04

def s_triangle():
    while True:
        t01 = []
        for i in range(0,3):
            b25 = rd.randint(1,100)
            t01.append(b25)
        t01.sort()
        a10 = t01[0] + t01[1]
        a11 = t01[2]
        if a10 > a11:
            break
    return t01

def normalize_text():
    
    #normalize the textto NFKD format
    text = unicodedata.normalize("NFKD", text)
    #encode using only ascii characters
    text = text.encode('ascii', 'ignore')
    #decode the textback to string, in the desired standard, in this case 'utf-8'
    text = text.decode('utf-8')
    #transform all characters in uppercase
    text = text.upper()

    return text

def specialint(text):
    while True:
        try:
            m2 = int(text)
            if m2 >= 0:
                break
            else:
                m2 = m2 * -1
                break
        except ValueError:
            if text.strip().isalpha():
                m2 = npvalid(text)
                break
            else:
                text = input(error)
    return m2

#Mundo 3













