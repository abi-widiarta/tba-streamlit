import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center;'>Lexical Analyzer/Parser</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Tugas Besar TBA IF-45-09</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Kelompok 9</h4>", unsafe_allow_html=True)
st.divider()

statusValid = '<p style="color:Green; font-size: 20px; text-align: center;">Kode yang anda input benar!</p>'
statusInvalid = '<p style="color:Red; font-size: 20px; text-align: center;">Kode yang anda input salah!</p>'

st.markdown("<h5 style='text-align: center;'>Program lexical analyzer/parser untuk sintaks perulangan \"while-do\" dalam bahasa c++</h5>", unsafe_allow_html=True)

st.write('Copy this code: ')
code = '''while (x<y) {
    x++;
}
    '''
st.code(code, language='cpp')

text=st.text_area("Input Code : ", placeholder="Input code")

statement1 = ['while', '(', '<var>', '<operator>', '<var>', ')', '{', '<var>', '+', '+', ';', '}']
statement2 = ['while', '(', '<var>', '<operator>', '<var>', ')', '{', '<var>', '-', '-', ';', '}']
head = []
state = []
statement = []

text = list(text)
# st.write(text)

i = 0
valid = True
currState = 'q0'
if st.button('Analyze'):
    while i < len(text) and valid == True:
        if currState == 'q0':
            if text[i] == 'w':
                head.append(text[i])
                state.append(currState)
                currState = 'q1'
                i += 1
            else:
                valid = False
        elif currState == 'q1':
            if text[i] == 'h':
                head.append(text[i])
                state.append(currState)
                currState = 'q2'
                i += 1
            else:
                valid = False
        elif currState == 'q2':
            if text[i] == 'i':
                head.append(text[i])
                state.append(currState)
                currState = 'q3'
                i += 1
            else:
                valid = False
        elif currState == 'q3':
            if text[i] == 'l':
                head.append(text[i])
                state.append(currState)
                currState = 'q4'
                i += 1
            else:
                valid = False
        elif currState == 'q4':
            if text[i] == 'e':
                head.append(text[i])
                state.append(currState)
                currState = 'q5'
                i += 1
                statement.append("while")
            else:
                valid = False
        elif currState == 'q5':
            if text[i] == '(':
                head.append(text[i])
                state.append(currState)
                currState = 'q6'
                i += 1
                statement.append('(')
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q6':
            if text[i] == 'x':
                head.append(text[i])
                state.append(currState)
                currState = 'q7'
                i += 1
                statement.append("<var>")
            elif text[i] == 'y':
                head.append(text[i])
                state.append(currState)
                currState = 'q7'
                i += 1
                statement.append("<var>")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q7':
            if text[i] == '<':
                head.append(text[i])
                state.append(currState)
                currState = 'q8'
                i += 1
                statement.append("<operator>")
            elif text[i] == '>':
                head.append(text[i])
                state.append(currState)
                currState = 'q8'
                i += 1
                statement.append("<operator>")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q8':
            if text[i] == 'x':
                head.append(text[i])
                state.append(currState)
                currState = 'q9'
                i += 1
                statement.append("<var>")
            elif text[i] == 'y':
                head.append(text[i])
                state.append(currState)
                currState = 'q9'
                i += 1
                statement.append("<var>")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q9':
            if text[i] == ')':
                head.append(text[i])
                state.append(currState)
                currState = 'q10'
                i += 1
                statement.append(")")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q10':
            if text[i] == '{':
                head.append(text[i])
                state.append(currState)
                currState = 'q11'
                i += 1
                statement.append("{")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q11':
            if text[i] == 'x':
                head.append(text[i])
                state.append(currState)
                currState = 'q12'
                i += 1
                statement.append("<var>")
            elif text[i] == 'y':
                head.append(text[i])
                state.append(currState)
                currState = 'q12'
                i += 1
                statement.append("<var>")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q12':
            if text[i] == '+':
                head.append(text[i])
                state.append(currState)
                currState = 'q13'
                i += 1
                statement.append("+")
            elif text[i] == '-':
                head.append(text[i])
                state.append(currState)
                currState = 'q13'
                i += 1
                statement.append("+")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q13':
            if text[i] == '+':
                head.append(text[i])
                state.append(currState)
                currState = 'q15'
                i += 1
                statement.append("+")
            else:
                valid = False
        elif currState == 'q14':
            if text[i] == '-':
                head.append(text[i])
                state.append(currState)
                currState = 'q16'
                i += 1
                statement.append("-")
            else:
                valid = False
        elif currState == 'q15':
            if text[i] == ';':
                head.append(text[i])
                state.append(currState)
                currState = 'q17'
                i += 1
                statement.append(";")
            else:
                valid = False
        elif currState == 'q16':
            if text[i] == ';':
                head.append(text[i])
                state.append(currState)
                currState = 'q17'
                i += 1
                statement.append(";")
            else:
                valid = False
        elif currState == 'q17':
            if text[i] == '}':
                head.append(text[i])
                state.append(currState)
                currState = 'q18'
                i += 1
                statement.append("}")
            elif text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False
        elif currState == 'q18':
            if text[i] == ' ':
                head.append("space")
                state.append(currState)
                i += 1
            elif text[i] == '\n':
                head.append("space")
                state.append(currState)
                i += 1
            else:
                valid = False

    if statement == statement1 or statement == statement2:
        susunan = True
    else:
        susunan = False

    if valid:
        if len(statement) < len(statement1):
            st.write(pd.DataFrame({
                'State': state,
                'Parse' : head
            }))
            st.write("^")
            if len(statement) == 8 or len(statement) == 9:
                st.write("Error, Expected + or - after", text[i-1])
                st.markdown(statusInvalid, unsafe_allow_html=True)
            else:
                if text[i-1] == '' or text[i-1] == ' ' or text[i-1] == '\n':
                    st.write("Error, Expected", statement1[len(statement)], "after space")
                else:
                    st.write("Error, Expected", statement1[len(statement)], "after", text[i-1])
                st.markdown(statusInvalid, unsafe_allow_html=True)

        else:
            st.write(pd.DataFrame({
                'State': state,
                'Parse' : head
            }))
            st.markdown(statusValid, unsafe_allow_html=True)
    else:
        st.write(pd.DataFrame({
                'State': state,
                'Parse' : head
        }))
        st.write("^Token salah")
        st.markdown(statusInvalid, unsafe_allow_html=True)

