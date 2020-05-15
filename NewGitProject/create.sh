#! /bin/bash

if [ -z "$1" ]
then
    echo "ERROR:"
    echo "Provide the project name"
    exit 0
fi

echo "Github password:"
read -s password

cd ~/Documents/GitHub/
python ~/Documents/GitHub/Automation/NewGitProject/github.py $1 $password
mkdir $1
cd $1
git init
echo "# $1" >> README.md
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/dutrad/$1.git
git push -u origin master
code .
