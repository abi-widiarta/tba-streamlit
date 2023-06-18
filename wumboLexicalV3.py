import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

kata = input("wumbo:")
kata = list(kata)
i = 0
valid = True

currState = 'q0'
while i < len(kata) and valid == True:
    if currState == 'q0':
        if kata[i] == 'w':
            currState = 'q1'
            i += 1
        elif kata[i] == '{':
            currState = 'q10'
            print("{")
            i += 1
        elif kata[i] == '}':
            print("}")
            currState = 'q10'
            i += 1
        elif kata[i] == '(':
            currState = 'q10'
            print("(")
            i += 1
        elif kata[i] == ')':
            currState = 'q10'
            print(")")
            i += 1
        elif kata[i] == '+':
            currState = 'q5'
            print("+")
            i += 1
        elif kata[i] == '-':
            currState = 'q7'
            print("-")
            i += 1
        elif kata[i] == 'x':
            currState = 'q10'
            print("x")
            i += 1
        elif kata[i] == 'y':
            currState = 'q10'
            print("y")
            i += 1
        elif kata[i] == '<':
            currState = 'q10'
            print("<")
            i += 1
        elif kata[i] == '>':
            currState = 'q10'
            print(">")
            i += 1
        elif kata[i] == ' ':
            currState = 'q0'
            i += 1
        else:
            valid = False
    elif currState == 'q1':
        if kata[i] == 'h':
            currState = 'q2'
            i += 1
        else:
            valid = False
    elif currState == 'q2':
        if kata[i] == 'i':
            currState = 'q3'
            i += 1
        else:
            valid = False
    elif currState == 'q3':
        if kata[i] == 'l':
            currState = 'q4'
            i += 1
        else:
            valid = False
    elif currState == 'q4':
        if kata[i] == 'e':
            currState = 'q10'
            print("while")
            i += 1
        else:
            valid = False
    elif currState == 'q5':
        if kata[i] == '+':
            currState = 'q6'
            print("+")
            i += 1
        else:
            valid = False
    elif currState == 'q6':
        if kata[i] == ';':
            currState = 'q10'
            print(";")
            i += 1
        else:
            valid = False
    elif currState == 'q7':
        if kata[i] == '-':
            currState = 'q8'
            print("-")
            i += 1
        else:
            valid = False
    elif currState == 'q8':
        if kata[i] == ';':
            currState = 'q10'
            print(";")
            i += 1
        else:
            valid = False
    elif currState == 'q10':
        if kata[i] == 'w':
            currState = 'q1'
            i += 1
        elif kata[i] == '(':
            currState = 'q0'
            i += 1
        elif kata[i] == '+':
            currState = 'q5'
            print("+")
            i += 1
        elif kata[i] == '-':
            currState = 'q7'
            print("-")
            i += 1
        elif kata[i] == 'x':
            currState = 'q0'
            print("x")
            i += 1
        elif kata[i] == 'y':
            currState = 'q0'
            print("y")
            i += 1
        elif kata[i] == '<':
            currState = 'q0'
            print("<")
            i += 1
        elif kata[i] == '>':
            currState = 'q0'
            print(">")
            i += 1
        elif kata[i] == '}':
            currState = 'q10'
            print('}')
            i += 1
        elif kata[i] == ' ':
            currState = 'q0'
            i += 1
        else:
            valid = False
    print(currState)
#print(kata[i])


if currState == 'q10': valid = True
print(valid)