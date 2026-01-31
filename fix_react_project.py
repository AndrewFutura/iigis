import os
from pathlib import Path

def fix_react_project():
    base_path = Path("C:/Projects/stroycompany/frontend")
    
    print("🛠️ Восстанавливаю структуру React проекта...")
    
    # 1. Создаем папки
    folders = [
        "public",
        "src",
        "src/pages",
        "src/pages/public",
        "src/components",
        "src/styles",
        "src/assets"
    ]
    
    for folder in folders:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Папка: {folder}")
    
    # 2. Создаем package.json
    package_json = base_path / "package.json"
    package_content = '''{
  "name": "stroy-master-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "devDependencies": {
    "react-scripts": "5.0.1"
  },
  "browserslist": {
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
  }
}'''
    
    with open(package_json, 'w', encoding='utf-8') as f:
        f.write(package_content)
    print("✓ Создан: package.json")
    
    # 3. Создаем index.html
    index_html = base_path / "public" / "index.html"
    html_content = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ИГИИС - Цифровые решения</title>
    <link rel="icon" href="favicon.ico">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
</head>
<body>
    <noscript>Для работы приложения необходим JavaScript. Пожалуйста, включите JavaScript в настройках браузера.</noscript>
    <div id="root"></div>
</body>
</html>'''
    
    with open(index_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✓ Создан: public/index.html")
    
    # 4. Создаем favicon.ico (пустой, чтобы не было ошибок)
    favicon = base_path / "public" / "favicon.ico"
    if not favicon.exists():
        # Создаем пустой файл
        with open(favicon, 'wb') as f:
            f.write(b'')
        print("✓ Создан: public/favicon.ico")
    
    # 5. Создаем App.js
    app_js = base_path / "src" / "App.js"
    app_content = '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './styles/global.css';

// Страницы будут добавляться позже
function App() {
  return (
    <Router>
      <div className="App">
        <header style={{ padding: '20px', background: '#478ac9', color: 'white' }}>
          <h1>ИГИИС - Цифровые решения</h1>
          <p>Система цифровизации инженерных изысканий</p>
        </header>
        
        <main style={{ padding: '20px' }}>
          <Routes>
            <Route path="/" element={
              <div>
                <h2>Главная страница</h2>
                <p>React приложение успешно запущено! 🎉</p>
                <div style={{ marginTop: '20px', padding: '20px', background: '#f5f5f5', borderRadius: '8px' }}>
                  <h3>Следующие шаги:</h3>
                  <ul>
                    <li>Добавьте ваши HTML/CSS страницы</li>
                    <li>Настройте маршрутизацию</li>
                    <li>Подключите бэкенд API</li>
                  </ul>
                </div>
              </div>
            } />
          </Routes>
        </main>
        
        <footer style={{ padding: '20px', background: '#333', color: 'white', marginTop: '40px' }}>
          <p>ООО "ИГИИС" • г. Москва</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;'''
    
    with open(app_js, 'w', encoding='utf-8') as f:
        f.write(app_content)
    print("✓ Создан: src/App.js")
    
    # 6. Создаем index.js
    index_js = base_path / "src" / "index.js"
    index_content = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);'''
    
    with open(index_js, 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("✓ Создан: src/index.js")
    
    # 7. Создаем глобальные стили
    global_css = base_path / "src" / "styles" / "global.css"
    css_content = '''/* Глобальные стили для проекта ИГИИС */
@import url('https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Open Sans', sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
}

h1, h2, h3, h4 {
  font-family: 'Roboto', sans-serif;
  margin-bottom: 15px;
}

.App {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}

/* Стили конструктора Nicepage (если будут использоваться) */
.u-body {
  font-size: 16px;
}

.u-xl-mode {
  font-size: 16px;
}

/* Адаптивность */
@media (max-width: 768px) {
  body {
    font-size: 14px;
  }
}'''
    
    with open(global_css, 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("✓ Создан: src/styles/global.css")
    
    print("\n" + "="*60)
    print("✅ СТРУКТУРА ПРОЕКТА ВОССТАНОВЛЕНА!")
    print("="*60)
    
    # 8. Инструкции
    print(f"\n🚀 ИНСТРУКЦИИ ПО ЗАПУСКУ:")
    print(f"1. Перейдите в папку фронтенда:")
    print(f"   cd C:\\Projects\\stroycompany\\frontend")
    print(f"")
    print(f"2. Удалите старые зависимости (если были проблемы):")
    print(f"   del /q node_modules 2>nul")
    print(f"   del package-lock.json 2>nul")
    print(f"")
    print(f"3. Установите зависимости:")
    print(f"   npm install")
    print(f"")
    print(f"4. Запустите React:")
    print(f"   npm start")
    print(f"")
    print(f"5. Откройте браузер: http://localhost:3000")
    
    # 9. Создаем bat файл для автоматического запуска
    bat_file = base_path.parent / "start_react.bat"
    bat_content = '''@echo off
echo ========================================
echo   АВТОМАТИЧЕСКИЙ ЗАПУСК REACT ПРОЕКТА
echo ========================================
echo.

cd /d "C:\\Projects\\stroycompany\\frontend"

echo Проверяю структуру проекта...
if not exist "public\\index.html" (
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
'''
    
    with open(bat_file, 'w', encoding='utf-8') as f:
        f.write(bat_content)
    print(f"\n📁 Создан файл для запуска: start_react.bat")
    print(f"   Запустите его двойным кликом!")

if __name__ == "__main__":
    fix_react_project()