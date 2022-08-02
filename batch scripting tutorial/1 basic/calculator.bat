@echo off
:a
echo ________Calculator________
echo.
set /p expression= Enter expression to calculate:
set /a ans=%expression%
echo.
echo = %ans%
echo
pause
cls
goto a