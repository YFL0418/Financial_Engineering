import numpy as np
import QuantLib as ql
import matplotlib.pyplot as plt
#請使用者輸入行使價格、市場無風險利率、選擇權期間、以及Hull-White Model衡量利率有關的參數、以及種類買、賣權種類
print("This is a calculator of price of option by incorporating Hull-White model.")
strike_price=float(input("Please enter the strike price: "))
risk_free=float(input("Please enter the current risk-free interest rate (yearly): "))
year=float(input("Please enter the duration of option: "))
a=float(input("Please enter the value of a in HW model: "))
sigma_hw=float(input("Please give tthe value of sigma in HW model): "))
forward_rate=float(input("Please enter the mean forward rate: "))
sigma=float(input("Please enter the daily volatitlity of stock: "))
S0=float(input("Please enter the current stock price:"))
date=int(input("Please enter the date today (yyyymmdd):"))
#以下參考自http://gouthamanbalaraman.com/blog/hull-white-simulation-quantlib-python.html，根據Hull White Model建立short rate的樣本路徑
timestep = int(360*year)
T = timestep
dt=0.01
day_count = ql.Thirty360()
d=int(date%100)
m=int(((date-date%100)%10000)/100)
y=int((date-date%100-((date-date%100)%10000))/10000)
todays_date = ql.Date(d,m,y)
ql.Settings.instance().evaluationDate = todays_date
spot_curve = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)
ql.Settings.instance().evaluationDate = todays_date
spot_curve = ql.FlatForward(todays_date, ql.QuoteHandle(ql.SimpleQuote(forward_rate)), day_count)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)
hw_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma_hw)
rng = ql.GaussianRandomSequenceGenerator(ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator()))
seq = ql.GaussianPathGenerator(hw_process, year, timestep, rng, False)
def generate_paths(num_paths, timestep):
    arr = np.zeros((num_paths, timestep+1))
    for i in range(num_paths):
        sample_path = seq.next()
        path = sample_path.value()
        time = [path.time(j) for j in range(len(path))]
        value = [path[j] for j in range(len(path))]
        arr[i, :] = np.array(value)
    return np.array(time), arr
#以下是將利率過程帶入產生股價的樣本路徑
def genBrownPath (T, mu, sigma, S0, dt):
    n=round(T/dt)
    W = np.random.standard_normal(size = n)
    S=S0
    S_process=[S0]
    m=0
    for k in range(n):
        m=m+1
        l=int((k-k%100)/100)
        S=S*(1+mu[l]*dt/360+W[k]*sigma*np.sqrt(dt))
        if m%100==0:
            S_process.append(S)
    return S, S_process
#設定欲計算路徑的總數，求出任一條路徑履約時的價值並利用無風險利率折現再取平均求得選擇權的價格
num_paths = 1000
time, paths = generate_paths(num_paths, timestep)
for i in range(num_paths):
    plt.title("Short Rate Process")
    plt.plot(time, paths[i, :], lw=1, alpha=1)
plt.show()
stock_price=np.zeros((num_paths,int(round(T/dt)/100)+1))
accumulated_future_cash_flow_call=0
accumulated_future_cash_flow_put=0
for i in range(num_paths):
    a,b=genBrownPath (T,paths[i,:], sigma, S0, dt)
    stock_price[i,:]=b
    if a>=strike_price:
        accumulated_future_cash_flow_call+=a-strike_price
    else:
        accumulated_future_cash_flow_put+=strike_price-a
discount=np.exp(-risk_free*year)
print("The price of call option is "+str(round(accumulated_future_cash_flow_call*discount/num_paths,3))+".")
print("The price of put option is "+str(round(accumulated_future_cash_flow_put*discount/num_paths,3))+".")
for i in range(num_paths):
    plt.title("Stock Price Process")
    plt.plot(time, stock_price[i, :], lw=1, alpha=1)
plt.show()


