@ echo off

set /A global_variable = 10
echo GV = %global_variable%

SETLOCAL
set /A local_variable = 90
set /A local_variable = %local_variable% + 10
echo LV = %local_variable%
ENDLOCAL

