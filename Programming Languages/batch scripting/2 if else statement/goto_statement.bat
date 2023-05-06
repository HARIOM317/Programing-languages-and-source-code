@echo off
set /A a = 100
if %a%==50 goto :labelone
if %a%==100 goto :labeltwo

:labelone
echo The value of a is 50

exit /b 0

:labeltwo 
echo The value of a is 100
