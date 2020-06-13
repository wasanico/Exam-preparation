import re
import sys

# Exo 1


tel = r'[0][1-9]\d{6}' #begin with a 0 then next number is not 0 then 6 numbers
nbint = r'-?[1-9]\d*'   #with optional minus no 0 at the start 

def phone():
    p = re.compile(tel)
    phone = input("enter your phone number (for ex : 04798695) :")
    print(p.match(phone))    
    if p.match(phone) == None :
        recall()
def recall():
    phone()    
def entier():
    p = re.compile(nbint)
    number = "-7564644654"
    print(p.match(number))

# recall()
# entier()


#Exo 2

numbers = r'\d+'
def findnumbers():
    p = re.compile(numbers)
    with open("labo 2 texte.txt") as file:
        for a, line in enumerate(file):
            if len(p.findall(line)):
                print( "line ",a+1, ": ", p.findall(line))
# findnumbers()

#Exo 3


url = "https://www.google.com/dio"
lien = r'(?P<protocol>[^./:]+)://(?P<domain>[^/]+)(?:/(?P<path>.*))?'

def decompose():
    u = re.compile(lien)
    groups = ["protocol","domain","path"]
    result = u.match(url)
    for group in groups:
        if(result.group(group)) is not None :
            print(group.capitalize(), result.group(group))
# decompose()  
        

# mini projet : mots croisés
lines = [
    r'(EC|CD)[ABS]',
    r'.[GROS]+',
    r'C?[KS]+'
]
columns = [
    r'[^CBF](MC|XD)',
    r'[CRI]*[ACK]',
    r'[AEIOU]*S'
]
answers = [
    ["E","C","A"],      #Line0[col0, col1, col2]
    ["M","R","O"],      #line1[col0 etc]
    ["C","K","S"]
]

separator = ''
def checkregexcrossword(linesregex, columnregex, answer):
    for a, l in enumerate(linesregex) :
        p = re.compile(l)
        # print("at line",a,":",l,"and answer is :",separator.join(answer[a]),"result :",p.match(separator.join(answer[a])))
        if (p.match(separator.join(answer[a]))) is not None:
            for b, c in enumerate(columnregex) :
                word = [list(row) for row in zip(*reversed(answer))]
                for rev in word:
                    rev.reverse()
                
                q = re.compile(c)
                
                
                print("at line",a,":",l,"and column",b,":",c,"answer :",answer[a][b],"result :",p.match(separator.join(answer[a])),"hello there",q.match(separator.join(word[b])))

checkregexcrossword(lines, columns, answers)