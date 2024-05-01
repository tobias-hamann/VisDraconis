@echo off

cd ../../../../

git checkout main

git status

git pull

git status

git checkout %COMPUTERNAME%

git merge main -m "Merge main into %COMPUTERNAME%"

timeout /t 5

exit