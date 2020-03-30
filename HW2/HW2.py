while True:
    print("This is a calculator of yield to maturity, spot rate, and forward rate.")
    choice=int(input("If you'd like to calculate yield to maturity of one bond, then please enter 1.\nIf you'd like to calculate spot rate generated by one zero coupon bond, then please enter 2.\nIf you'd like to calculate forward rate based on a set of bonds, then please enter 3.\nNow you can enter. "))
    if choice==1:
        current_bond_price=float(input("Please enter the cuurent bond price: "))
        par_value=float(input("Please enter the par value of the bond: "))
        coupon_rate=float(input("Please enter the coupon rate(%): "))
        year_to_maturity=float(input("Please enter year to maturity of the bond: "))
        proceed_payment_method=int(input("If proceeds are paid annually, please enter 1.\nIf proceeds are paid semiannually, please enter 2.\nIf proceeds are paid quarterly, please enter 4.\n Now please enter: "))
        coupon=par_value*coupon_rate/100/proceed_payment_method
        total_payment_times=year_to_maturity*proceed_payment_method
        ytm=0
        for a in range(0,10,1):
            a=a/10
            time=1
            present_value=0
            while time<=total_payment_times-1:
                present_value+=coupon/(1+(a/proceed_payment_method))**time
                time+=1
            present_value+=(coupon+par_value)/(1+(a/proceed_payment_method))**total_payment_times
            if present_value<current_bond_price:
                ytm=a-0.1
                break
            else:
                continue
        for a in range(int(ytm*100),int((ytm+0.1)*100)+1,1):
            a=a/100
            time=1
            present_value=0
            while time<=total_payment_times-1:
                present_value+=coupon/(1+(a/proceed_payment_method))**time
                time+=1
            present_value+=(coupon+par_value)/(1+(a/proceed_payment_method))**total_payment_times
            if present_value<current_bond_price:
                ytm=a-0.01
                break
            else:
                continue
        for a in range(int(ytm*1000),int((ytm+0.01)*1000)+1,1):
            a=a/1000
            time=1
            present_value=0
            while time<=total_payment_times-1:
                present_value+=coupon/(1+(a/proceed_payment_method))**time
                time+=1
            present_value+=(coupon+par_value)/(1+(a/proceed_payment_method))**total_payment_times
            if present_value<current_bond_price:
                ytm=a-0.001
                break
            else:
                continue
        for a in range(int(ytm*10000),int((ytm+0.001)*10000)+1,1):
            a=a/10000
            time=1
            present_value=0
            while time<=total_payment_times-1:
                present_value+=coupon/(1+(a/proceed_payment_method))**time
                time+=1
            present_value+=(coupon+par_value)/(1+(a/proceed_payment_method))**total_payment_times
            if present_value<current_bond_price:
                ytm=a-0.0001
                break
            else:
                continue
        for a in range(int(ytm*100000),int((ytm+0.0001)*100000),1):
            a=a/100000
            time=1
            present_value=0
            while time<=total_payment_times-1:
                present_value+=coupon/(1+(a/proceed_payment_method))**time
                time+=1
            present_value+=(coupon+par_value)/(1+(a/proceed_payment_method))**total_payment_times
            if present_value<current_bond_price:
                ytm=a-0.00001
                break
            else:
                continue    
        YTM_percent=ytm*100
        print("Yield to maturity is "+str(YTM_percent)+"%")
    elif choice==2:
        year_to_maturity=int(input("Please enter year to maturity of the zero coupon bond: "))
        current_bond_price=float(input("Please enter the price of unit coupon bond: "))
        for a in range(0,100000+1,1):
            if 1/(1+(a/100000))**year_to_maturity<current_bond_price:
                spot_rate=round((a/100000-0.000001)*100,3)
                print(str(year_to_maturity)+" year spot rate of interest is "+str(spot_rate)+"%")
                break
            else:
                continue
    elif choice==3:
        year_to_maturity=float(input("Please enter the number of years you want to know the variation of forward rate.\n"))
        period_duration=float(input("Please enter the duration of each period during which forward rate are calculated.(annually, 1, semiannually, 2, and quarterly, 4)\n"))
        number_of_bond_required=int(year_to_maturity*period_duration)
        print("To calculate forward rate for each period in the future, please enter the data of bonds in order of short to long year to maturity.")
        bond_number=0
        spot_rate=[]
        while bond_number<=number_of_bond_required-1:
            bond_number+=1
            current_bond_price=float(input("Please enter the bond price: "))
            par_value=float(input("Please enter the par value of the bond: "))
            coupon_rate=float(input("Please enter the coupon rate(%): "))
            if period_duration==1:
                coupon_rate=coupon_rate/100/1
            elif period_duration==2:
                coupon_rate=coupon_rate/100/2
            elif period_duration==4:
                coupon_rate=coupon_rate/100/4
            if bond_number==1:
                f_01=current_bond_price/((coupon_rate+1)*par_value)
                spot_rate.append(f_01)
            elif bond_number>1:
                present_value=0
                for n in range(1, bond_number,1):
                    present_value+=coupon_rate*par_value*spot_rate[n-1]
                f=(current_bond_price-present_value)/((coupon_rate+1)*par_value)
                spot_rate.append(f)
        import sys
        from prettytable import PrettyTable
        spot_rate.insert(0,1)
        if period_duration==1:
            table= PrettyTable(["year\year",*range(0,number_of_bond_required+1,1)])
        elif period_duration==2:
            table= PrettyTable(["half-year\half-year",*range(0,number_of_bond_required+1,1)])
        elif period_duration==4:
            table= PrettyTable(["quarter\quarter",*range(0,number_of_bond_required+1,1)])
        for n in range(0,number_of_bond_required+1,1):
            row=[]
            row.append(n)
            time=0
            while time<n:
                row.append("-")
                time+=1
            time=0
            for k in spot_rate:
                if time==0:
                    row.append(1-1)
                    time=time+1
                elif time>0:
                    if period_duration==1:
                        row.append(round(((1/(k/spot_rate[0]))**(1/time)-1)*100,3))
                        time=time+1
                    elif period_duration==2:
                        row.append(round((((1/(k/spot_rate[0]))**(1/time)-1)*2)*100,3))
                        time=time+1
                    elif period_duration==4:
                        row.append(round((((1/(k/spot_rate[0]))**(1/time)-1)*4)*100,3))
                        time=time+1
            table.add_row(row)
            spot_rate.pop(0)
        print(table)
            
                    

            
                              
                
    
        
    