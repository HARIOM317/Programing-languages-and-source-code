@echo off
set /A first = 50
set /A second = 100
set /A third = 153
rem return addition
set /A sum = %first% + %second%     
echo Sum = %sum%
rem return substraction
set /A sum = %first% - %second%   
echo substraction = %sum%
rem return multiplication
set /A sum = %first% * %second%
echo multiplication = %sum%
rem return division
set /A sum = %second% / %first%
echo division = %sum%
rem return remainder
set /A sum = %third% %% %first%
echo remainder = %sum%
