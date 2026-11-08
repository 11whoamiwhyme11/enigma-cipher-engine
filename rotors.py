# rotors.py
# 5 original German Enigma rotors, each as a list of dictionaries.
# Each dictionary in the list contains a single mapping: {input_letter: output_letter}.

rotor_1 = [
    {'A': 'E'}, {'B': 'K'}, {'C': 'M'}, {'D': 'F'}, {'E': 'L'}, {'F': 'G'}, {'G': 'D'}, {'H': 'Q'},
    {'I': 'V'}, {'J': 'Z'}, {'K': 'N'}, {'L': 'T'}, {'M': 'O'}, {'N': 'W'}, {'O': 'Y'}, {'P': 'H'},
    {'Q': 'X'}, {'R': 'U'}, {'S': 'S'}, {'T': 'P'}, {'U': 'A'}, {'V': 'I'}, {'W': 'B'}, {'X': 'R'},
    {'Y': 'C'}, {'Z': 'J'}
]

rotor_2 = [
    {'A': 'A'}, {'B': 'J'}, {'C': 'D'}, {'D': 'K'}, {'E': 'S'}, {'F': 'I'}, {'G': 'R'}, {'H': 'U'},
    {'I': 'X'}, {'J': 'B'}, {'K': 'L'}, {'L': 'H'}, {'M': 'W'}, {'N': 'T'}, {'O': 'M'}, {'P': 'C'},
    {'Q': 'Q'}, {'R': 'G'}, {'S': 'Z'}, {'T': 'N'}, {'U': 'P'}, {'V': 'Y'}, {'W': 'F'}, {'X': 'V'},
    {'Y': 'O'}, {'Z': 'E'}
]

rotor_3 = [
    {'A': 'B'}, {'B': 'D'}, {'C': 'F'}, {'D': 'H'}, {'E': 'J'}, {'F': 'L'}, {'G': 'C'}, {'H': 'P'},
    {'I': 'R'}, {'J': 'T'}, {'K': 'X'}, {'L': 'V'}, {'M': 'Z'}, {'N': 'N'}, {'O': 'Y'}, {'P': 'E'},
    {'Q': 'I'}, {'R': 'W'}, {'S': 'G'}, {'T': 'A'}, {'U': 'K'}, {'V': 'M'}, {'W': 'U'}, {'X': 'S'},
    {'Y': 'Q'}, {'Z': 'O'}
]

rotor_4 = [
    {'A': 'E'}, {'B': 'S'}, {'C': 'O'}, {'D': 'V'}, {'E': 'P'}, {'F': 'Z'}, {'G': 'J'}, {'H': 'A'},
    {'I': 'Y'}, {'J': 'Q'}, {'K': 'U'}, {'L': 'I'}, {'M': 'R'}, {'N': 'H'}, {'O': 'X'}, {'P': 'L'},
    {'Q': 'N'}, {'R': 'F'}, {'S': 'T'}, {'T': 'G'}, {'U': 'K'}, {'V': 'D'}, {'W': 'C'}, {'X': 'M'},
    {'Y': 'W'}, {'Z': 'B'}
]

rotor_5 = [
    {'A': 'V'}, {'B': 'Z'}, {'C': 'B'}, {'D': 'R'}, {'E': 'G'}, {'F': 'I'}, {'G': 'T'}, {'H': 'Y'},
    {'I': 'U'}, {'J': 'P'}, {'K': 'S'}, {'L': 'D'}, {'M': 'N'}, {'N': 'H'}, {'O': 'L'}, {'P': 'X'},
    {'Q': 'A'}, {'R': 'W'}, {'S': 'M'}, {'T': 'J'}, {'U': 'Q'}, {'V': 'O'}, {'W': 'F'}, {'X': 'E'},
    {'Y': 'C'}, {'Z': 'K'}
]

rev_rotor_1 = [
    {'A': 'U'}, {'B': 'W'}, {'C': 'Y'}, {'D': 'G'}, {'E': 'A'}, {'F': 'D'}, {'G': 'F'}, {'H': 'P'},
    {'I': 'V'}, {'J': 'Z'}, {'K': 'B'}, {'L': 'E'}, {'M': 'C'}, {'N': 'K'}, {'O': 'M'}, {'P': 'T'},
    {'Q': 'H'}, {'R': 'X'}, {'S': 'S'}, {'T': 'L'}, {'U': 'R'}, {'V': 'I'}, {'W': 'N'}, {'X': 'Q'},
    {'Y': 'O'}, {'Z': 'J'}
]

rev_rotor_2 = [
    {'A': 'A'}, {'B': 'J'}, {'C': 'P'}, {'D': 'C'}, {'E': 'Z'}, {'F': 'W'}, {'G': 'R'}, {'H': 'L'},
    {'I': 'F'}, {'J': 'B'}, {'K': 'D'}, {'L': 'K'}, {'M': 'O'}, {'N': 'T'}, {'O': 'Y'}, {'P': 'U'},
    {'Q': 'Q'}, {'R': 'G'}, {'S': 'E'}, {'T': 'N'}, {'U': 'H'}, {'V': 'X'}, {'W': 'M'}, {'X': 'I'},
    {'Y': 'V'}, {'Z': 'S'}
]

rev_rotor_3 = [
    {'A': 'T'}, {'B': 'A'}, {'C': 'G'}, {'D': 'B'}, {'E': 'P'}, {'F': 'C'}, {'G': 'S'}, {'H': 'D'},
    {'I': 'Q'}, {'J': 'E'}, {'K': 'U'}, {'L': 'F'}, {'M': 'V'}, {'N': 'N'}, {'O': 'Z'}, {'P': 'H'},
    {'Q': 'Y'}, {'R': 'I'}, {'S': 'X'}, {'T': 'J'}, {'U': 'W'}, {'V': 'L'}, {'W': 'R'}, {'X': 'K'},
    {'Y': 'O'}, {'Z': 'M'}
]

rev_rotor_4 = [
    {'A': 'H'}, {'B': 'Z'}, {'C': 'W'}, {'D': 'V'}, {'E': 'A'}, {'F': 'R'}, {'G': 'T'}, {'H': 'N'},
    {'I': 'L'}, {'J': 'G'}, {'K': 'U'}, {'L': 'P'}, {'M': 'X'}, {'N': 'Q'}, {'O': 'C'}, {'P': 'E'},
    {'Q': 'J'}, {'R': 'M'}, {'S': 'B'}, {'T': 'S'}, {'U': 'K'}, {'V': 'D'}, {'W': 'Y'}, {'X': 'O'},
    {'Y': 'I'}, {'Z': 'F'}
]

rev_rotor_5 = [
    {'A': 'Q'}, {'B': 'C'}, {'C': 'Y'}, {'D': 'L'}, {'E': 'X'}, {'F': 'W'}, {'G': 'E'}, {'H': 'N'},
    {'I': 'F'}, {'J': 'T'}, {'K': 'Z'}, {'L': 'O'}, {'M': 'S'}, {'N': 'M'}, {'O': 'V'}, {'P': 'J'},
    {'Q': 'U'}, {'R': 'D'}, {'S': 'K'}, {'T': 'G'}, {'U': 'I'}, {'V': 'A'}, {'W': 'R'}, {'X': 'P'},
    {'Y': 'H'}, {'Z': 'B'}
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mr_1=0
mr_2=0
mr_3=0

def r1(x : list , y : int):
    pointer=x[y]
    return alphabet.index(list(pointer.values())[0])

def r2(x : list , y : int):
    pointer=x[y]
    return alphabet.index(list(pointer.values())[0])

def r3(x : list , y : int):
    pointer=x[y]
    return alphabet.index(list(pointer.values())[0])

def r1_set(x:str):
    global rotor_1,rev_rotor_1
    for i in rotor_1:
        for k,v in i.items():
            if k==x:
                g=rotor_1.index(i)
                rotor_1=rotor_1[g:]+rotor_1[:g]
                rev_rotor_1=rev_rotor_1[g:]+rev_rotor_1[:g]

def r2_set(x:str):
    global rotor_2,rev_rotor_2
    for i in rotor_2:
        for k,v in i.items():
            if k==x:
                g=rotor_2.index(i)
                rotor_2=rotor_2[g:]+rotor_2[:g]
                rev_rotor_2=rev_rotor_2[g:]+rev_rotor_2[:g]

def r3_set(x:str):
    global rotor_3,rev_rotor_3
    for i in rotor_3:
        for k,v in i.items():
            if k==x:
                g=rotor_3.index(i)
                rotor_3=rotor_3[g:]+rotor_3[:g]
                rev_rotor_3=rev_rotor_3[g:]+rev_rotor_3[:g]

def r4_set(x:str):
    global rotor_4,rev_rotor_4
    for i in rotor_4:
        for k,v in i.items():
            if k==x:
                g=rotor_4.index(i)
                rotor_4=rotor_4[g:]+rotor_4[:g]
                rev_rotor_4=rev_rotor_4[g:]+rev_rotor_4[:g]

def r5_set(x:str):
    global rotor_5,rev_rotor_5
    for i in rotor_5:
        for k,v in i.items():
            if k==x:
                g=rotor_5.index(i)
                rotor_5=rotor_5[g:]+rotor_5[:g]
                rev_rotor_5=rev_rotor_5[g:]+rev_rotor_5[:g]

def step_rotor(x:list,y:list,z:list,a:list,b:list,c:list):
    global mr_1, mr_2, mr_3
    mr_1+=1
    x.insert(0,x.pop())
    a.insert(0,a.pop())
    if mr_1==26:
        mr_1=0
        mr_2+=1
        y.insert(0,y.pop())
        b.insert(0,b.pop())
        if mr_2==26:
            mr_2=0
            mr_3+=1
            z.insert(0,z.pop())
            c.insert(0,c.pop())
            if mr_3==26:
                mr_3=0
