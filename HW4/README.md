# 關於HW4
[執行檔](https://github.com/YFL0418/Financial_Engineering/blob/master/HW4/HW4.py)

[執行畫面](https://github.com/YFL0418/Financial_Engineering/blob/master/HW4/hw4%E5%9F%B7%E8%A1%8C%E7%95%AB%E9%9D%A2.jpg)

Price of put is 2.86. Price of call is 12.806.

作業流程簡述如下:
1. 先進行離散發放的股利折現調整基底股票的價格，並一樣假設調整後的股價符合幾何布朗運動
2. 使用Black Scholes formula計算賣權價格 (過程同上課講義)
3. 使用put call parity算買權價格

步驟三有用到put call parity。put call parity的原理就是未來現金流的吻合。在各個狀態下，賣權和一單位股票的資產組合與買權和到期日支付exercise price零息票債券的組合所帶來的現金流一樣，則兩組合的現值也相同。

上述將離散發放的股利直接折現的方法在低股利的狀況下可使調整後的股價仍近似幾何布朗運動(於是BS model可直接應用)，然而在高股利時此假設可能不滿足(偏誤可能達9%)，底下附上一篇使用Monte Carlo Method處理此問題的論文。該論文提及的方法為建立同樣的binomial random walk去模擬，但在發放股利的前一期使用插值法(做調整。 [論文](https://ris.utwente.nl/ws/portalfiles/portal/6787112/Vellekoop06efficient.pdf)

關於random walk模擬布朗運動可以參考Donsker's theorem，我有試過用Prokhorov's theorem去證明，另一證明方法可以參考Durrett's Probability: Theory and Examples，使用Prokhorov's theorem的證明過程較為簡潔，但須了解一部分的拓樸學和測度論，如果對測度tightness和Ascoli Azela theorem有所了解應能很快上手。

關於Ito formula中的各項微分型式的變換可以參考HW3中所附上的筆記

*所謂的模擬就是weak convergence概念的應用
