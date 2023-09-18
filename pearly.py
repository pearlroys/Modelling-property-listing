coeff corr =
//x̄
var __muX =calculate(AVERAGE(YourTable[x]))
//ȳ
var __muY=calculate(AVERAGE(YourTable[y]))
//numerator
var __numerator  =  sumx('YourTable',( [x]-__muX)*([y]-__muY))
//denominator
var __denominator=  SQRT(sumx('YourTable',([x]-__muX)^2)*sumx('YourTable',([y]-__muY)^2))
return
divide(__numerator,__denominator)



R-squared Measure =
VAR ActualValues = SUM('YourTable'[Life Expectancy])
VAR PredictedValues = SUMX('YourTable', 'YourTable'[Predicted Life Expectancy])
VAR Residuals = ActualValues - PredictedValues
VAR SSTotal = SUMX('YourTable', ('YourTable'[Life Expectancy] - AVERAGE('YourTable'[Life Expectancy]))^2)
VAR SSResiduals = SUMX('YourTable', Residuals^2)
RETURN
1 - (SSResiduals / SSTotal)
