@echo off
@echo Left String
set str=Good-Morning
echo.%str%
set str=%str:~0,4%
echo.%str%