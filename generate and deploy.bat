@echo off
echo ================================
echo   Running Homework Generator
echo ================================

:: ---------------------------
:: Run Node.js script
:: ---------------------------
node scripts\generate-homeworks.js
if errorlevel 1 (
    echo ⚠️ Something went wrong in the generator. Aborting.
    pause
    exit /b 1
)

echo.
echo ✅ Homeworks JSON updated

:: ---------------------------
:: Pull remote changes (handle unrelated histories)
:: ---------------------------
git pull origin main --allow-unrelated-histories

:: ---------------------------
:: Stage all changes
:: ---------------------------
git add .

:: ---------------------------
:: Ask for commit message
:: ---------------------------
set /p commitmsg=Enter commit message: 

:: ---------------------------
:: Commit changes
:: ---------------------------
git commit -m "%commitmsg%"

:: ---------------------------
:: Push to GitHub
:: ---------------------------
git push origin main

echo.
echo ================================
echo   All changes pushed to GitHub!
echo   Your GitHub Pages site should update shortly.
echo ================================
pause
