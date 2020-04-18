"This is a calculator for pricing calls on a non-dividend-paying stock by appling BOPM."
import numpy as np
user_input=input("Please enter the information of the call (S, u, d, X, n, r): ")
user_input=user_input.strip('()')
call_information=user_input.split(',')
S=float(call_information[0])
u=float(call_information[1])
d=float(call_information[2])
X=float(call_information[3])
n=int(call_information[4])
r=float(call_information[5])
min_strike=np.log(X/(S*d**n))/np.log(u/d)
k=0
while k<min_strike:
    k=k+1
min_strike=k
if min_strike>n:
    print("the price of call=0")
p=(np.exp(r/100)-d)/(u-d)
R=np.exp(r/100*n)
b=p**min_strike*(1-p)**(n-min_strike)
for k in range(min_strike+1,n+1):
    b=b*k
for k in range(1,n-min_strike+1):
    b=b/k
lower_limit=S*u**min_strike*d**(n-min_strike)
C=b*(lower_limit-X)/R
for k in range(min_strike+1, n+1):
    b=b*p*(n-k+1)/(1-p)/k
    lower_limit=lower_limit*u/d
    C=C+b*(lower_limit-X)/R
print("the price of call="+str(round(C,3)))
"Put call parity"
P=C+X/R-S
print("the price of put with the same exercise condition="+str(round(P,3)))
    

    




