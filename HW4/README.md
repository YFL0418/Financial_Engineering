# 關於HW4
[執行檔](https://github.com/YFL0418/Financial_Engineering/blob/master/HW4/HW4.py)

Price of put is 2.86. Price of call is 12.806.

作業流程很簡單簡述如下:
1. 先進行離散發放的股利折現調整基底股票的價格，並一樣假設股價符合幾何布朗運動
2. 使用Black Scholes formula計算賣權價格 (過程同上課ppt)
3. 使用put call parity算買權價格

作業的最後一部分有用到put call parity。put call parity的原理就是未來現金流的吻合。在各個狀態下，賣權和一單位股票的資產組合與買權和到期日支付exercise price零息票債券的組合到期日所帶來的現金流一樣，則兩組合的現值也相同，於是我們就有put call parity。
