@echo off

set /A first = 5
set /A second = 10

if %first% EQU %second% echo First is equal to second
if %first% neq %second% echo First is not equal to second
if %first% lss %second% echo First is less than second
if %first% leq %second% echo First is less than or equal to second
if %first% gtr %second% echo First is greater than second
if %first% geq %second% echo First is greater than or equal to second