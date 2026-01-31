from pathlib import Path

def create_css_files():
    base = Path("stroycompany/frontend/src/components/Layout")
    
    css_files = {
        "Header.css": """/* Header стили на основе вашего HTML */
.header {
  background-color: white;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.u-sheet-1 {
  max-width: 1200px;
  margin: 0 auto;
  padding: 15px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Логотип */
.u-image-1 {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.u-logo-image-1 {
  width: 60px;
  height: 60px;
  border-radius: 8px;
  object-fit: contain;
}

/* Навигация */
.u-menu-1 {
  display: flex;
  align-items: center;
}

.u-nav-1 {
  display: flex;
  list-style: none;
  gap: 30px;
  margin: 0;
  padding: 0;
}

.u-nav-item {
  margin: 0;
}

.u-nav-link {
  text-decoration: none;
  color: #333;
  font-weight: 600;
  font-size: 16px;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s;
}

.u-nav-link:hover {
  color: #478ac9;
  background-color: rgba(71,138,201,0.1);
}

/* Контакты в хедере */
.u-btn-1, .u-btn-2 {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: #333;
  font-size: 14px;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s;
}

.u-btn-1:hover, .u-btn-2:hover {
  color: #478ac9;
  background-color: rgba(71,138,201,0.1);
}

.u-icon {
  margin-right: 5px;
}

/* Поиск */
.u-search-1 {
  display: flex;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 5px;
}

.u-search-input {
  border: none;
  padding: 8px;
  width: 200px;
  outline: none;
}

.u-search-button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
}

/* Адаптивность */
@media (max-width: 992px) {
  .u-sheet-1 {
    flex-wrap: wrap;
    gap: 15px;
  }
  
  .u-nav-1 {
    gap: 15px;
  }
}

@media (max-width: 768px) {
  .u-nav-1 {
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: white;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    padding: 20px;
    display: none;
  }
  
  .u-menu-open .u-nav-1 {
    display: flex;
  }
  
  .menu-collapse {
    display: block !important;
  }
  
  .u-search-input {
    width: 150px;
  }
}

@media (max-width: 480px) {
  .u-sheet-1 {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
  
  .u-search-1 {
    width: 100%;
  }
  
  .u-search-input {
    width: 100%;
  }
}""",
        
        "Footer.css": """/* Footer стили */
.footer {
  background-color: #2c3e50;
  color: white;
  padding: 40px 0 20px;
  margin-top: 60px;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 40px;
}

.footer-section {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.footer-section h3 {
  color: #478ac9;
  font-size: 24px;
  margin-bottom: 10px;
}

.footer-section p {
  color: #bdc3c7;
  line-height: 1.6;
}

.footer-section a {
  color: #bdc3c7;
  text-decoration: none;
  transition: color 0.3s;
}

.footer-section a:hover {
  color: #478ac9;
}

.footer-bottom {
  max-width: 1200px;
  margin: 40px auto 0;
  padding: 20px;
  border-top: 1px solid #34495e;
  text-align: center;
  color: #95a5a6;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}""",
        
        "Layout.css": """/* Layout общие стили */
.layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  padding: 20px;
}

/* Переменные для цветов из вашего HTML */
:root {
  --primary-color: #478ac9;
  --secondary-color: #2c3e50;
  --text-color: #333;
  --light-gray: #f5f5f5;
  --border-color: #ddd;
}

/* Классы из вашего HTML для совместимости */
.u-body {
  font-family: 'Open Sans', sans-serif;
  font-size: 16px;
  color: var(--text-color);
}

.u-xl-mode {
  /* Стили для режима конструктора */
}

.u-container-style {
  position: relative;
}

.u-similar-container {
  /* Общие стили для контейнеров */
}

/* Адаптивность */
@media (max-width: 768px) {
  .main-content {
    padding: 15px;
  }
}"""
    }
    
    # Создаем файлы
    for filename, content in css_files.items():
        filepath = base / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Создан: {filepath}")
    
    print("\n🎉 Все CSS файлы созданы!")
    print("\n📋 Следующие шаги:")
    print("1. Убедитесь что Header.js и Footer.js импортируют свои CSS:")
    print("   import './Header.css';")
    print("   import './Footer.css';")
    print("\n2. Запустите React: cd frontend && npm start")

if __name__ == "__main__":
    create_css_files()