# 🚀 GitHub Integration & Deployment Guide

## Step 1: Create a New GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository (e.g., "edumate-chatbot")
5. Add a description: "AI-powered study assistant for students"
6. Make it public or private (your choice)
7. **DO NOT** initialize with README, .gitignore, or license (we already have these)
8. Click "Create repository"

## Step 2: Connect Your Local Project to GitHub

After creating the repository, GitHub will show you commands. Use these in your terminal:

```bash
# Initialize git in your project (if not already done)
git init

# Add all files to git
git add .

# Make your first commit
git commit -m "Initial commit: EduMate AI Study Assistant"

# Add your GitHub repository as origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Set Up Environment Variables for Deployment

### For Vercel:
1. Go to [Vercel](https://vercel.com)
2. Import your GitHub repository
3. In the deployment settings, add environment variable:
   - Name: `VITE_OPENROUTER_API_KEY`
   - Value: Your OpenRouter API key
4. Deploy!

### For Netlify:
1. Go to [Netlify](https://netlify.com)
2. Connect your GitHub repository
3. Build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
4. In Environment variables, add:
   - `VITE_OPENROUTER_API_KEY`: Your OpenRouter API key
5. Deploy!

### For GitHub Pages:
1. In your GitHub repository, go to Settings → Pages
2. Source: Deploy from a branch
3. Branch: `gh-pages` (you'll need to set this up with GitHub Actions)

## Step 4: GitHub Actions for Automatic Deployment (Optional)

Create `.github/workflows/deploy.yml` for automatic deployment to GitHub Pages:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Build
      run: npm run build
      env:
        VITE_OPENROUTER_API_KEY: ${{ secrets.VITE_OPENROUTER_API_KEY }}
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./dist
```

Then add your API key as a repository secret:
1. Go to your repo → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `VITE_OPENROUTER_API_KEY`
4. Value: Your OpenRouter API key

## 🔒 Important Security Notes

- **Never commit your `.env` file** - it's already in `.gitignore`
- **Use environment variables** for all sensitive data
- **The API key is now properly configured** to use environment variables instead of being hardcoded

## 🎯 Quick Commands Summary

```bash
# 1. Initialize and commit
git init
git add .
git commit -m "Initial commit: EduMate AI Study Assistant"

# 2. Connect to GitHub (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main

# 3. For future updates
git add .
git commit -m "Your commit message"
git push
```

## ✅ Verification Checklist

- [ ] Repository created on GitHub
- [ ] Local project connected to GitHub
- [ ] `.env` file is NOT committed (check .gitignore)
- [ ] Environment variables set up on deployment platform
- [ ] App builds successfully (`npm run build`)
- [ ] Deployment platform connected to GitHub repo

Need help with any of these steps? Let me know which deployment platform you prefer and I can provide more specific guidance!