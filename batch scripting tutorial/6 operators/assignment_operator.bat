@echo off
set /A number1 = 50
set /A number2 = 100
set /A number3 = 200
set /A number4 = 300
set /A number5 = 400

set /A number1+=50
echo %number1%
set /A number2-=50
echo %number2%
set /A number3*=50
echo %number3%
set /A number4/=50
echo %number4%
set /A number5%%=50
echo %number5%