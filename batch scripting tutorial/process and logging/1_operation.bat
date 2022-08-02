@echo off
REM To get the list of all the running processes
TASKLIST

REM Logging in a file
TASKLIST > processes.txt

REM Tell you the memory usage greater than a number
REM Here /fi displays a set of tasks that match a given criteria specified by the filter
tasklist /fi "memusage gt 50000" > processesGT50000.txt

REM killing a process
rem syntax Taskkill /f /im name.exe
Taskkill /f /im notepad.exe

REM starting a new process
rem syntax START "title" [/D path][options] " command" [parameters]
START notepad.exe "Notepadfile.txt"
