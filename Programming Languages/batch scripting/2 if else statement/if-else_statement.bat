@echo off
set str1=hariom
set str2=string2
if %str1%==hariom (
    echo "The value of variable is string1"
) else (
    echo "Unknown value"
)

if %str2%==string3 (
    echo "This is correct value"
) else (
    echo "This is incorrect value"
)