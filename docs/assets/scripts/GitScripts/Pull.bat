@echo off

cd ../../../../

git checkout main

git status

git pull

git status

git checkout -b %COMPUTERNAME%

timeout /t 5

exit