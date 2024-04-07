@echo off

cd ../../../../

git checkout main

git status

git pull

git status

timeout /t 5

exit