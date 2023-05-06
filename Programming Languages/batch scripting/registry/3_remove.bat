@echo off
REG DELETE HKEY_CURRENT_USER\Console /v TestData /f
REG QUERY HKEY_CURRENT_USER\Console /v TestData