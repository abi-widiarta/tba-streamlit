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

def notFound(cekList, cek):
    for i in range(len(cekList)):
        if cekList[i].head == cek:
            return False
    return True

def wumbo(text):
    currState = 'q0'
    i = 0
    while i < len(text):
        if currState == 'q0':
            if text[i] == 'w':
                currState = 'q1'
                i+=1
            elif text[i] == '(' or text[i] == ')' or text[i] == '{' or text[i] == '}' or text[i] == '+' or text[i] == '-' or text[i] == ';' or text[i] == 'x' or text[i] == 'y' or text[i] == '>' or text[i] == '<':
                if notFound(listToken, text[i]):
                    temp = token(text[i], True)
                    listToken.append(temp)
                head.append(text[i])
                state.append(currState)
                if text[i] == 'x' or text[i] == 'y':
                    statement.append("<var>")
                elif text[i] == '>' or text[i] == '<':
                    statement.append("<operator>")
                else:
                    statement.append(text[i])
                i+=1
            elif text[i] == ' ':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], True)
                    listToken.append(temp)
                i+=1
        elif currState == 'q1':
            if text[i] == 'h':
                currState = 'q2'
                i+=1
            elif text[i] == ' ':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], True)
                    listToken.append(temp)
                currState = 'q0'
                i+=1
        elif currState == 'q2':
            if text[i] == 'i':
                currState = 'q3'
                i+=1
            elif text[i] == ' ':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], True)
                    listToken.append(temp)
                currState = 'q0'
                i+=1
        elif currState == 'q3':
            if text[i] == 'l':
                currState = 'q4'
                i+=1
            elif text[i] == ' ':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], True)
                    listToken.append(temp)
                currState = 'q0'
                i+=1
        elif currState == 'q4':
            if text[i] == 'e':
                if notFound(listToken, "while"):
                    temp = token("while", True)
                    listToken.append(temp)
                head.append("while")
                state.append(currState)
                statement.append("while")
                currState = 'q0'
                i+=1
            elif text[i] == ' ':
                i+=1
            else:
                if notFound(listToken, text[i]):
                    temp = token(text[i], True)
                    listToken.append(temp)
                currState = 'q0'
                i+=1


statement = []
statement1 = ['while', '(', '<var>', '<operator>', '<var>', ')', '{', '<var>', '+', '+', ';', '}']
statement2 = ['while', '(', '<var>', '<operator>', '<var>', ')', '{', '<var>', '-', '-', ';', '}']
head = []
state = []

class token:
    def __init__(self, head, valid):
        self.head = head
        self.valid = valid

listToken = []

text = list(text)
valid = True
currState = 'q0'

if st.button('Analyze'):
    wumbo(text)

    st.write("Token\tValid")
    for i in range(len(listToken)):
        if listToken[i].valid:
            st.write(listToken[i].head,"\t True")
        else:
            st.write(listToken[i].head,"\t False")
            valid = False

    if statement == statement1 or statement == statement2:
        susunan = True
    else:
        susunan = False

    if valid:
        if statement == statement1 or statement == statement2:
            st.write("Grammar: ", end='')
            for i in range(len(statement)):
                st.write(statement[i], end=' ')
            st.write("Susunan token sudah sesuai grammar")

            st.write("Parser")
            for i in range(len(head)):
                st.write(head[i])
        else:
            st.write("Susunan token: ", end='')
            for i in range(len(statement)):
                st.write(statement[i], end=' ')
            i = 0
            stop = False
            while i <= len(statement) and stop == False:
                if i == 0 and statement[0] != "while":
                    st.write("Error, Expected while at start of statement")
                    stop = True
                elif (i == 8 and statement[i] != statement1[i]) and (i == 8 and statement[i] != statement2[i]):
                    st.write("Error, Expected + or - after <var>")
                    stop = True
                elif (i == 9 and statement[i] != statement1[i]) and statement[i-1] == '+':
                    st.write("Error, Expected + after +")
                    stop = True
                elif (i == 9 and statement[i] != statement2[i]) and statement[i-1] == '-':
                    st.write("Error, Expected - after -")
                    stop = True
                elif (statement[i] != statement1[i]) and (i != 8 and i != 9):
                    st.write("Error, Expected", statement1[i], "after", statement[i-1])
                    stop = True
                i += 1