#BS model
import math
S=75
X=65
r=0.06
vol=0.35
t=6/12
PV_d=1*math.exp(-r*1/12)+1*math.exp(-r*4/12)
adjusted_S=S-PV_d
d_1=(math.log(adjusted_S/X)+(r+1/2*vol**2)*t)/vol/t**(1/2)
d_2=d_1-vol*(t**(1/2))
nd1=(1+math.erf(-d_1/(2**0.5)))*0.5
nd2=(1+math.erf(-d_2/(2**0.5)))*0.5
put_price=X*math.exp(-r*t)*nd2-adjusted_S*nd1
#By put call parity
call_price=put_price+adjusted_S-X*math.exp(-r*t)
print("The price of put is "+str(round(put_price, 3))+".")
print("The price of call is "+str(round(call_price, 3))+".")







