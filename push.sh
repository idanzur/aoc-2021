#!/bin/sh
set -xe

DAY=$(basename $PWD)

git add .
git commit -m "day $DAY part $1"
git push origin main