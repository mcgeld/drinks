#!/bin/bash

echo "📌 Saving changes to dev branch..."
cd /var/www/websites/drinks

# Make sure we're on dev branch
git checkout dev

# Check if a commit message was provided
if [ -z "$1" ]; then
    COMMIT_MSG="Auto-save: $(date)"
else
    COMMIT_MSG="$1"
fi

# Add & commit changes with message
git add .
git commit -m "$COMMIT_MSG"

# Push to remote dev branch
git push origin dev

echo "✅ Changes saved to dev branch!"
