@echo off
echo ========================================
echo   АВТОМАТИЧЕСКИЙ ЗАПУСК REACT ПРОЕКТА
echo ========================================
echo.

cd /d "C:\Projects\stroycompany\frontend"

echo Проверяю структуру проекта...
if not exist "public\index.html" (
    echo ❌ ОШИБКА: Нет index.html
    echo Запустите fix_react_project.py для создания структуры
    pause
    exit /b 1
)

if not exist "node_modules" (
    echo Устанавливаю зависимости npm...
    call npm install
    if %errorlevel% neq 0 (
        echo ❌ Ошибка при установке зависимостей
        pause
        exit /b 1
    )
)

echo.
echo ========================================
echo   ЗАПУСКАЮ REACT НА ПОРТУ 3000
echo   Откройте браузер: http://localhost:3000
echo ========================================
echo.

call npm start

pause
