import streamlit as st
import pandas as pd

st.title('Lexical Analyzer')

kata = st.text_area("Input String : ", placeholder="Input String")
kata = list(kata)
i = 0
valid = True

currState = 'q0'

if st.button('Analyze'):
    while i < len(kata) and valid == True:
        if currState == 'q0':
            if kata[i] == 'w':
                currState = 'q1'
                i += 1
            elif kata[i] == '{':
                currState = 'q10'
                st.write("{")
                i += 1
            elif kata[i] == '}':
                st.write("}")
                currState = 'q10'
                i += 1
            elif kata[i] == '(':
                currState = 'q10'
                st.write("(")
                i += 1
            elif kata[i] == ')':
                currState = 'q10'
                st.write(")")
                i += 1
            elif kata[i] == '+':
                currState = 'q5'
                st.write("+")
                i += 1
            elif kata[i] == '-':
                currState = 'q7'
                st.write("-")
                i += 1
            elif kata[i] == 'x':
                currState = 'q10'
                st.write("x")
                i += 1
            elif kata[i] == 'y':
                currState = 'q10'
                st.write("y")
                i += 1
            elif kata[i] == '<':
                currState = 'q10'
                st.write("<")
                i += 1
            elif kata[i] == '>':
                currState = 'q10'
                st.write(">")
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
                st.write("while")
                i += 1
            else:
                valid = False
        elif currState == 'q5':
            if kata[i] == '+':
                currState = 'q6'
                st.write("+")
                i += 1
            else:
                valid = False
        elif currState == 'q6':
            if kata[i] == ';':
                currState = 'q10'
                st.write(";")
                i += 1
            else:
                valid = False
        elif currState == 'q7':
            if kata[i] == '-':
                currState = 'q8'
                st.write("-")
                i += 1
            else:
                valid = False
        elif currState == 'q8':
            if kata[i] == ';':
                currState = 'q10'
                st.write(";")
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
                st.write("+")
                i += 1
            elif kata[i] == '-':
                currState = 'q7'
                st.write("-")
                i += 1
            elif kata[i] == 'x':
                currState = 'q0'
                st.write("x")
                i += 1
            elif kata[i] == 'y':
                currState = 'q0'
                st.write("y")
                i += 1
            elif kata[i] == '<':
                currState = 'q0'
                st.write("<")
                i += 1
            elif kata[i] == '>':
                currState = 'q0'
                st.write(">")
                i += 1
            elif kata[i] == '}':
                currState = 'q10'
                st.write('}')
                i += 1
            elif kata[i] == ' ':
                currState = 'q0'
                i += 1
            else:
                valid = False
        st.write(currState)
    #st.write(kata[i])
    
    if currState == 'q10': valid = True
    st.write(valid)
    
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))
