def wumbo(text):
    currState = 'q0'
    i = 0
    while i < len(text):
        if currState == 'q0':
            if text[i] == 'w':
                currState = 'q1'
                i+=1
            elif text[i] == '(' or text[i] == ')' or text[i] == '{' or text[i] == '}' or text[i] == '+' or text[i] == '-' or text[i] == ';' or text[i] == 'x' or text[i] == 'y' or text[i] == '>' or text[i] == '<':
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
                temp = token(text[i], False)
                listToken.append(temp)
                i+=1
        elif currState == 'q1':
            if text[i] == 'h':
                currState = 'q2'
                i+=1
            elif text[i] == ' ':
                i+=1
            else:
                temp = token(text[i], False)
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
                temp = token(text[i], False)
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
                temp = token(text[i], False)
                listToken.append(temp)
                currState = 'q0'
                i+=1
        elif currState == 'q4':
            if text[i] == 'e':
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
                temp = token(text[i], False)
                listToken.append(temp)
                currState = 'q0'
                i+=1

baris = 3
text = ""
for i in range(baris):
    text+=input()

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



wumbo(text)

print("Token\tValid")
for i in range(len(listToken)):
    if listToken[i].valid:
        print(listToken[i].head,"\t True")
    else:
        print(listToken[i].head,"\t False")
        valid = False

if statement == statement1 or statement == statement2:
    susunan = True
else:
    susunan = False

if valid:
    if statement == statement1 or statement == statement2:
        print("Grammar: ", end='')
        for i in range(len(statement)):
            print(statement[i], end=' ')
        print("\nSusunan token sudah sesuai grammar")
    else:
        print("Susunan token: ", end='')
        for i in range(len(statement)):
            print(statement[i], end=' ')
        for i in range(len(statement)):
            if (i == 8 and statement[i] != statement1[i]) and (i == 8 and statement[i] != statement2[i]):
                print("Error, Expected + or - after <var>")
            elif (i == 9 and statement[i] != statement1[i]) and statement[i-1] == '+':
                print("Error, Expected + after +")
            elif (i == 9 and statement[i] != statement2[i]) and statement[i-1] == '-':
                print("Error, Expected - after -")
            elif (statement[i] != statement1[i]) and (i != 8 and i != 9):
                print(i)
                print("Error, Expected", statement1[i], "after", statement[i-1])