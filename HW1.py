print('本金平均攤還試算')
print('本金平均攤還法是將本金平均在貸款期間償還，每期償還的本金均相同，而每期所攤還的利息卻因累積未攤還之本金逐漸減少而減少，因此，每期所攤還的本利和會越來越少。')
print('請您按照順序分別輸入數據，即可得出每期攤還所需費用')
principal_w=float(input('本金(萬): '))
principal=principal_w*10000
period=int(input('期數(年): '))
interest_rate_percent=float(input('年利率(%): '))
interest_rate=interest_rate_percent/1200
remain_principal=principal
should_interest=0
should_principal=round((principal/12)/period, 3)
sum_interest_prinicpal=0
name='本金'+str(principal_w)+'萬元'+str(period)+'年期'+'年利率'+str(interest_rate_percent)+'%'
import csv
with open(name+'.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow([' ','本 金(元)','利 息(元)','本金利息累計(元)'])
    first_row=[' ','本 金(元)','利 息(元)','本金利息累計(元)']
    for n in range(1, period*12+1):
        should_interest=round(remain_principal*interest_rate,3)
        sum_interest_prinicpal=sum_interest_prinicpal+should_principal+should_interest
        writer.writerow(['第'+str(n)+'期',should_principal,should_interest,sum_interest_prinicpal])
        remain_principal=remain_principal-should_principal
        
        


    
    
    
    
    
