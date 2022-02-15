# Python Program for compound interest
# method-1
# function method use
def compound(P,T,R):
    # formula of compound interest
    A=P*(1+R/100)**T
    CI=A-P
    print(CI) #output

print(compound(1200,2,5.4))

# method-2

# here enter the value of P,T,R
P=int(input('Enter the value of P: '))
T=int(input('Enter the value of T: '))
R=int(input('Enter the value of R: '))
# formula
A=P*(1+R/100)**T
CI=A-P
# output
print(CI)
