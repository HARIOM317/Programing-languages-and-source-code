@echo off

REG ADD HKEY_CURRENT_USER\Console /v TestData /d "This is an entry"
REG QUERY HKEY_CURRENT_USER\Console /v TestData