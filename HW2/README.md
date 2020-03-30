## 關於HW2
執行檔 [HW2](/https://github.com/YFL0418/Financial_Engineering/blob/master/HW2/HW2.py)

學習歷程、流程圖 [學習歷程](/https://github.com/YFL0418/Financial_Engineering/blob/master/HW2/HW2%E6%B5%81%E7%A8%8B%E5%9C%96%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B.ipynb)

使用者可以在執行檔中選擇計算YTM、spot rate、forward rate

若要計算YTM，使用者會被要求輸入一檔債券的資訊(市價、票面價值、coupon rate、天期、coupon支付方式)

測試YTM計算可以使用這個網站 [Yield to Maturity Calculator](https://www.calculatestuff.com/financial/bond-yield-calculator)

若要計算spot rate，使用者會被要求輸入一檔zero coupon bond的資訊(天期、單位coupon bond市價)

測試spot rate計算可以使用這個網站[Spot Rate](https://www.trignosource.com/finance/spot%20rate.html)

若要計算forward rate，使用者在選擇欲計算的年數和期間長短(一年、半年、或一季)，使用者會被要求依序輸入天期以期間長短為等差的債券資料(市價、票面價值、coupon rate)

測試forward rate對照表可以使用這組債券資料
|到期時間 |6月|半年|一年|
|--------|---|-----|-----|
|市價|99.50|98.03|102.91|
|票面價值|100|100|100|
|票面利率%|0|0|5|

測試正確值可參考[綠角財經筆記](http://greenhornfinancefootnote.blogspot.com/2010/08/how-to-compute-forward-rates-from.html)


