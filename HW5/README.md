## 關於HW5
[執行檔](https://github.com/YFL0418/Financial_Engineering/blob/master/HW5/HW5.py)

[學習歷程](https://github.com/YFL0418/Financial_Engineering/blob/master/HW5/Learning_process_HW5.pdf)

[流程圖](https://github.com/YFL0418/Financial_Engineering/blob/master/HW5/%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)

1.在執行檔裡預設所要跑的路徑數為1000條，此數值可以調整，跑的路徑數越多，其結果愈能收斂

2.執行過程中由於short rate跑出來是daily basis的路徑，因此請使用者輸入的股價波動率也使用daily basis，好處是易於統計收集和執行時不須轉換

3.以下是相關輸入輸出結果

輸入資料

(strike price, sigma, duration(year), sigma in Hull-White model, a, mean forward rate, current stock price, risk-free interest rate)=(100, 0.01, 0.5, 0.1, 0.1, 0.05, 120, 0.03)

輸出結果

[Short rate process](https://github.com/YFL0418/Financial_Engineering/blob/master/HW5/short%20rate%20process.png)

[Stock price process](https://github.com/YFL0418/Financial_Engineering/blob/master/HW5/stock%20price%20process.png)

兩圖的X軸單位為年份，Y軸則分別為short rate(instantaneous rate)和股價

Call price is 22.852.

Put price is 0.472.
