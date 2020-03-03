#!/bin/bash

#cat $1

cd ..

#pwd

#cat "./system_testing/$1"

python3 -m main < "./system_testing/$1"

cd ./system_testing

pwd
