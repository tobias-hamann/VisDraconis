@echo off

cd ../../../../

git checkout master

git status

git pull

git status

timeout /t 5

exit