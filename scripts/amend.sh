#!/bin/bash
set -e

git add .
git commit --amend
# git push -f

echo "Amend commit completed successfully."
