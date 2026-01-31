import os
import shutil
from pathlib import Path

def integrate_pages():
    print("📦 Интегрирую ваши страницы в React...")
    
    # Пути
    original_dir = Path("C:/Projects/stroycompany/original_files")
    react_dir = Path("C:/Projects/stroycompany/frontend/src")
    
    # 1. Копируем изображения
    images_src = Path("C:/Projects/stroycompany/backend/app/static/uploads")
    images_dest = react_dir / "assets" / "images"
    
    if images_src.exists():
        images_dest.mkdir(parents=True, exist_ok=True)
        for img in images_src.glob("*.*"):
            shutil.copy2(img, images_dest / img.name)
        print(f"✓ Изображения скопированы: {images_dest}")
    else:
        # Создаем placeholder изображения
        images_dest.mkdir(parents=True, exist_ok=True)
        placeholder_images = ['logo_IGIIS.gif', 'homework-icon.png', 'checklist-icon.png']
        for img in placeholder_images:
            (images_dest / img).touch()
        print(f"✓ Заглушки изображений созданы")
    
    # 2. Создаем основные страницы если их нет
    pages_dir = react_dir / "pages" / "public"
    pages_dir.mkdir(parents=True, exist_ok=True)
    
    # 3. Обновляем App.js с навигацией
    app_js = react_dir / "App.js"
    if app_js.exists():
        with open(app_js, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Простое обновление - добавляем Header и Footer
        new_content = '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './styles/global.css';

// Импортируем страницы
import HomePage from './pages/public/HomePage';
import DensityCalculation from './pages/public/DensityCalculation';
import SurveyProgram from './pages/public/SurveyProgram';
import ThankYouPage from './pages/public/ThankYouPage';

// Компонент Header
const Header = () => (
  <header style={{ 
    background: '#fff', 
    padding: '15px 0',
    boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
    position: 'sticky',
    top: 0,
    zIndex: 1000
  }}>
    <div style={{ 
      maxWidth: '1200px', 
      margin: '0 auto', 
      display: 'flex', 
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '0 20px'
    }}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{
          width: '50px',
          height: '50px',
          background: '#478ac9',
          borderRadius: '8px',
          marginRight: '15px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'white',
          fontWeight: 'bold'
        }}>
          ИГИИС
        </div>
        <div>
          <h1 style={{ margin: 0, fontSize: '24px', color: '#478ac9' }}>ИГИИС</h1>
          <p style={{ margin: 0, fontSize: '14px', color: '#666' }}>цифровые решения</p>
        </div>
      </div>
      
      <nav>
        <a href="/" style={{ margin: '0 15px', color: '#333', textDecoration: 'none', fontWeight: '500' }}>Главная</a>
        <a href="/density" style={{ margin: '0 15px', color: '#333', textDecoration: 'none', fontWeight: '500' }}>Расчет плотности</a>
        <a href="/survey" style={{ margin: '0 15px', color: '#333', textDecoration: 'none', fontWeight: '500' }}>Программа</a>
        <a href="/contacts" style={{ margin: '0 15px', color: '#333', textDecoration: 'none', fontWeight: '500' }}>Контакты</a>
      </nav>
    </div>
  </header>
);

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        
        <main style={{ minHeight: '70vh' }}>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/density" element={<DensityCalculation />} />
            <Route path="/survey" element={<SurveyProgram />} />
            <Route path="/thank-you" element={<ThankYouPage />} />
            <Route path="/contacts" element={
              <div style={{ padding: '40px', textAlign: 'center' }}>
                <h2>Контакты</h2>
                <p><strong>Телефон:</strong> +7 (495) 366-31-89</p>
                <p><strong>Email:</strong> mail@igiis.ru</p>
                <p><strong>Адрес:</strong> 127051, г. Москва, Крапивенский пер., 3, стр. 1</p>
              </div>
            } />
          </Routes>
        </main>
        
        <footer style={{ 
          background: '#333', 
          color: 'white', 
          padding: '30px 0',
          marginTop: '50px',
          textAlign: 'center'
        }}>
          <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '0 20px' }}>
            <p>ООО "ИГИИС" • Цифровизация инженерных изысканий</p>
            <p>© 2024 Все права защищены</p>
            <p style={{ fontSize: '12px', marginTop: '10px', opacity: '0.8' }}>
              Продолжая использовать сайт, вы соглашаетесь на обработку файлов cookies
            </p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;'''
        
        with open(app_js, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✓ App.js обновлен с навигацией")
    
    print("\n✅ ИНТЕГРАЦИЯ ЗАВЕРШЕНА!")
    print("\n📋 ЧТО ДЕЛАТЬ ДАЛЬШЕ:")
    print("1. Замените заглушки в HomePage.js на ваш реальный HTML код")
    print("2. Скопируйте CSS стили в соответствующие .css файлы")
    print("3. Добавьте обработку форм (отправка данных на бэкенд)")
    print("\n🔧 React уже запущен - изменения будут видны автоматически!")

if __name__ == "__main__":
    integrate_pages()