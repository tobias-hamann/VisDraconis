@echo off

cd ../../../../

git status

git add .

git commit -m "Update from %COMPUTERNAME%"

git push

git status

timeout /t 5

exit