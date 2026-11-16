#!/bin/bash
set -e

git add .
git commit -m "$1"
# git push -f

echo "Commit completed successfully."
