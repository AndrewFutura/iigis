import os
from pathlib import Path

def main():
    print("🔍 Проверяю структуру проекта...")
    print("=" * 50)
    
    # Текущая директория
    current_dir = Path.cwd()
    print(f"Текущая папка: {current_dir}")
    
    # Проверяем папку original_files
    original_dir = current_dir / "original_files"
    print(f"\n📁 Папка original_files: {original_dir}")
    print(f"Существует: {original_dir.exists()}")
    
    if original_dir.exists():
        print("\n📄 Файлы в original_files:")
        for file in original_dir.glob("*"):
            print(f"  - {file.name}")
    
    # Проверяем другие папки
    print(f"\n📁 Папка backend: {(current_dir / 'backend').exists()}")
    print(f"📁 Папка frontend: {(current_dir / 'frontend').exists()}")
    
    print("\n" + "=" * 50)
    print("🚀 Создаю структуру React вручную...")
    
    # Создаем базовую структуру
    frontend_dir = current_dir / "frontend"
    src_dir = frontend_dir / "src" / "pages" / "public"
    
    src_dir.mkdir(parents=True, exist_ok=True)
    
    # Создаем простые тестовые файлы
    test_js = src_dir / "TestPage.js"
    test_css = src_dir / "TestPage.css"
    
    test_js.write_text('''
import React from 'react';
import './TestPage.css';

const TestPage = () => {
  return (
    <div className="test-page">
      <h1>Тестовая страница React</h1>
      <p>Если вы видите это, значит React работает!</p>
    </div>
  );
};

export default TestPage;
''', encoding='utf-8')
    
    test_css.write_text('''
.test-page {
  padding: 20px;
  text-align: center;
}

.test-page h1 {
  color: #478ac9;
}
''', encoding='utf-8')
    
    print(f"✅ Создано: {test_js}")
    print(f"✅ Создано: {test_css}")
    
    # Создаем App.js
    app_js = frontend_dir / "src" / "App.js"
    app_js.parent.mkdir(parents=True, exist_ok=True)
    
    app_js.write_text('''
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import TestPage from './pages/public/TestPage';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<TestPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
''', encoding='utf-8')
    
    print(f"✅ Создано: {app_js}")
    
    # Создаем index.js
    index_js = frontend_dir / "src" / "index.js"
    index_js.write_text('''
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
''', encoding='utf-8')
    
    print(f"✅ Создано: {index_js}")
    
    # Создаем package.json
    package_json = frontend_dir / "package.json"
    package_json.write_text('''{
  "name": "igiis-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0"
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
}
''', encoding='utf-8')
    
    print(f"✅ Создано: {package_json}")
    
    # Создаем public/index.html
    public_dir = frontend_dir / "public"
    public_dir.mkdir(parents=True, exist_ok=True)
    
    index_html = public_dir / "index.html"
    index_html.write_text('''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ИГИИС - Цифровые решения</title>
</head>
<body>
    <div id="root"></div>
</body>
</html>
''', encoding='utf-8')
    
    print(f"✅ Создано: {index_html}")
    
    print("\n" + "=" * 50)
    print("🎉 БАЗОВАЯ СТРУКТУРА REACT СОЗДАНА!")
    print("=" * 50)
    
    print("\n🚀 Инструкции по запуску:")
    print("1. Перейдите в папку frontend: cd frontend")
    print("2. Установите зависимости: npm install")
    print("3. Запустите React: npm start")
    print("4. Откройте браузер: http://localhost:3000")
    
    print("\n📁 Созданная структура:")
    print("frontend/")
    print("├── src/")
    print("│   ├── pages/public/")
    print("│   │   ├── TestPage.js")
    print("│   │   └── TestPage.css")
    print("│   ├── App.js")
    print("│   └── index.js")
    print("├── public/")
    print("│   └── index.html")
    print("└── package.json")

if __name__ == "__main__":
    main()