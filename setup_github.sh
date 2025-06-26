#!/bin/bash

# GitHub Repository Setup Script
# Run this after creating your repository on GitHub

echo "🚀 Setting up GitHub repository for Python Web GUI App"
echo "=================================================="

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ Error: Please run this script from the python_web_app directory"
    exit 1
fi

# Get repository URL from user
echo "📝 Please enter your GitHub repository URL:"
echo "Example: https://github.com/varunmanik/python-web-gui-app.git"
read -p "Repository URL: " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "❌ Error: Repository URL cannot be empty"
    exit 1
fi

echo ""
echo "🔗 Adding remote origin..."
git remote add origin "$REPO_URL"

echo "📤 Pushing code to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Your code has been pushed to GitHub!"
    echo "✅ Repository URL: $REPO_URL"
    echo "✅ Branch: main"
    echo "✅ Files uploaded: 7"
    echo ""
    echo "🌐 You can now view your repository at:"
    echo "${REPO_URL%.git}"
else
    echo ""
    echo "❌ Error occurred during push. Please check:"
    echo "1. Repository URL is correct"
    echo "2. You have access to the repository"
    echo "3. Repository exists on GitHub"
    echo ""
    echo "💡 You can also push manually with:"
    echo "git push -u origin main"
fi

echo ""
echo "📚 Next steps:"
echo "1. Visit your GitHub repository"
echo "2. Add a description and topics"
echo "3. Share with others!"
echo "=================================================="
