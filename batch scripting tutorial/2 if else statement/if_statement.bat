@echo off

REM comparing numeric values

set /A a = 50
set /A b = 100
set /A sum = %a% + %b%
if %sum%==150 echo The sum is 150
if %sum%==100 echo The sum is 100

REM comparing string values


set str1=hariom
set str2=rajput
if %str1%==hariom echo This is correct
if %str2%==hariom echo This is incorrect