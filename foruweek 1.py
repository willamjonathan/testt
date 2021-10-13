#%% Algorithm and programming forum week 1
#%% William Jonathan M - L1CC
import math

#%% number 1
a = eval(input("Enter numerator, numerator >0 :"))
if a <= 0:
    print("Numerator value has to be > 0")
    a = eval(input("Please re-enter the value of Numerator, the value > 0 :"))
b = eval(input("Enter denominator, denominator >0 :"))
if b <= 0:
    print("Denominator value has to be > 0")
    b = eval(input("Please re-enter the value of Denominator, the value > 0 :"))

#%% number 2
from fractions import Fraction

c = math.gcd(a,b)
d = Fraction(a,b)
e = a%b
f = a//b
g = Fraction(e,b)
#i = math.gcd(e,b)

if b>a:
    print (a,"/",b,"is a proper fraction")
    if c != 1:
        print ("This proper fraction can be reduced to",d)

    else:
        print("This proper fraction can't be reduced any further")
if b<a :
    print(a,"/",b,"is an improper fraction")
    if c != 1 :
        if e != 0:
            print ("This improper fraction can be reduced to",d)
            print("The mixed number is",f,'and',g)
        if e == 0:
            print ("This improper fraction can be reduced to",d,'/',1)
            print ("The whole number is",d)
    elif c == 1 :
        if e != 0:
            print("This improper fraction can be reduced to",d,'/',1)
            print("The mixed number is",f,'and',g)
        if e == 0:
            print ("This improper fraction can't be reduced any further")
            print ("The whole number is",d)



