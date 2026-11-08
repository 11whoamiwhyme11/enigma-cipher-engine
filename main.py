from rotors import r1,r2,r3 ,rotor_1 ,rotor_2 ,rotor_3 ,rotor_4 ,rotor_5 ,rev_rotor_1 ,rev_rotor_2 ,rev_rotor_3 ,rev_rotor_4 ,rev_rotor_5 
from reflector import ref
from rotors import r1_set , r2_set , r3_set , r4_set , r5_set,step_rotor
from rotors import mr_1 , mr_2 ,mr_3
from plugboard import plugboard

r1_set("A")
r2_set("J")
r3_set("O")
r4_set("P")
r5_set("Z")
l = {
    'A': 'B', 'B': 'A',
    'C': 'D', 'D': 'C'
}

while True:
    n=input("enter the charcter to encrypt :")
    p=0
    s=plugboard(l,n.upper())
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in alphabet:
        if s==i: 
            p=alphabet.index(i)
    if n=="!":
        break
    else:
        step_rotor(rotor_1,rotor_2,rotor_3,rev_rotor_1,rev_rotor_2,rev_rotor_3)
        n1=r1(rotor_3,p)
        n2=r2(rotor_2,n1)
        n3=r3(rotor_1,n2)
        n4=ref(n3)
        n5=r3(rev_rotor_1,n4)
        n6=r2(rev_rotor_2,n5)
        n7=r1(rev_rotor_3,n6)
        print(plugboard(l,alphabet[n7]))