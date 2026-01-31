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
pause