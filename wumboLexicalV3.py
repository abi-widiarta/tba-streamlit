import streamlit as st
import pandas as pd

st.title('Lexical Analyzer')

kata = st.text_area("Input String : ", placeholder="Input String")
kata = list(kata)
i = 0
valid = True

currState = 'q0'
allState = []

if st.button('Analyze'):
    while i < len(kata) and valid == True:
        if currState == 'q0':
            if kata[i] == 'w':
                currState = 'q1'
                allState.append(currState)
                i += 1
            elif kata[i] == '{':
                currState = 'q10'
                allState.append(currState)
                st.write("{")
                i += 1
            elif kata[i] == '}':
                st.write("}")
                currState = 'q10'
                allState.append(currState)
                i += 1
            elif kata[i] == '(':
                currState = 'q10'
                allState.append(currState)
                st.write("(")
                i += 1
            elif kata[i] == ')':
                currState = 'q10'
                allState.append(currState)
                st.write(")")
                i += 1
            elif kata[i] == '+':
                currState = 'q5'
                allState.append(currState)
                st.write("+")
                i += 1
            elif kata[i] == '-':
                currState = 'q7'
                allState.append(currState)
                st.write("-")
                i += 1
            elif kata[i] == 'x':
                currState = 'q10'
                allState.append(currState)
                st.write("x")
                i += 1
            elif kata[i] == 'y':
                currState = 'q10'
                allState.append(currState)
                st.write("y")
                i += 1
            elif kata[i] == '<':
                currState = 'q10'
                allState.append(currState)
                st.write("<")
                i += 1
            elif kata[i] == '>':
                currState = 'q10'
                allState.append(currState)
                st.write(">")
                i += 1
            elif kata[i] == ' ':
                currState = 'q0'
                allState.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q1':
            if kata[i] == 'h':
                currState = 'q2'
                allState.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q2':
            if kata[i] == 'i':
                currState = 'q3'
                allState.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q3':
            if kata[i] == 'l':
                currState = 'q4'
                allState.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q4':
            if kata[i] == 'e':
                currState = 'q10'
                allState.append(currState)
                st.write("while")
                i += 1
            else:
                valid = False
        elif currState == 'q5':
            if kata[i] == '+':
                currState = 'q6'
                allState.append(currState)
                st.write("+")
                i += 1
            else:
                valid = False
        elif currState == 'q6':
            if kata[i] == ';':
                currState = 'q10'
                allState.append(currState)
                st.write(";")
                i += 1
            else:
                valid = False
        elif currState == 'q7':
            if kata[i] == '-':
                currState = 'q8'
                allState.append(currState)
                st.write("-")
                i += 1
            else:
                valid = False
        elif currState == 'q8':
            if kata[i] == ';':
                currState = 'q10'
                allState.append(currState)
                st.write(";")
                i += 1
            else:
                valid = False
        elif currState == 'q10':
            if kata[i] == 'w':
                currState = 'q1'
                allState.append(currState)
                i += 1
            elif kata[i] == '(':
                currState = 'q0'
                allState.append(currState)
                i += 1
            elif kata[i] == '+':
                currState = 'q5'
                allState.append(currState)
                st.write("+")
                i += 1
            elif kata[i] == '-':
                currState = 'q7'
                allState.append(currState)
                st.write("-")
                i += 1
            elif kata[i] == 'x':
                currState = 'q0'
                allState.append(currState)
                st.write("x")
                i += 1
            elif kata[i] == 'y':
                currState = 'q0'
                allState.append(currState)
                st.write("y")
                i += 1
            elif kata[i] == '<':
                currState = 'q0'
                allState.append(currState)
                st.write("<")
                i += 1
            elif kata[i] == '>':
                currState = 'q0'
                allState.append(currState)
                st.write(">")
                i += 1
            elif kata[i] == '}':
                currState = 'q10'
                allState.append(currState)
                st.write('}')
                i += 1
            elif kata[i] == ' ':
                currState = 'q0'
                allState.append(currState)
                i += 1
            else:
                valid = False
        st.write(currState)
    #st.write(kata[i])
    
    if currState == 'q10': valid = True
    st.write(valid)
    
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'State': [1, 2, 3, 4],
        'Parse': [10, 20, 30, 40]
    }))
