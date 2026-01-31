# fix_image_paths.py
import os
import re
from pathlib import Path

def fix_css_images():
    print("🖼️ Исправляю пути к изображениям в CSS...")
    
    css_dir = Path("frontend/src/pages/public")
    
    # Находим все CSS файлы
    css_files = list(css_dir.glob("*.css"))
    
    for css_file in css_files:
        print(f"\n📄 Обрабатываю: {css_file.name}")
        
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Исправляем пути к изображениям
        # Было: url("/images/файл.jpg") 
        # Стало: url("/assets/images/файл.jpg") или убираем путь если файла нет
        
        # Вариант 1: Исправляем на правильный путь
        fixed_content = re.sub(
            r'url\("/images/([^"]+)"\)',
            r'url("/assets/images/\1")',
            content
        )
        
        # Вариант 2: Для теста можно заменить на простой цвет
        if 'background-image' in fixed_content:
            fixed_content = re.sub(
                r'background-image:\s*url\([^)]+\);',
                'background-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%);',
                fixed_content
            )
        
        # Сохраняем исправленный файл
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"  ✅ Исправлен: {css_file.name}")

def create_placeholder_images():
    """Создает placeholder изображения если реальных нет"""
    
    images_dir = Path("frontend/src/assets/images")
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Создаем простые SVG изображения как placeholder
    placeholders = {
        'global-business-internet-network-connection-iot-internet-things-business-intelligence-concept-busines-global-network-futuristic-technology-background-ai-generative.jpg': '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#667eea"/>
      <stop offset="100%" stop-color="#764ba2"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#grad1)"/>
  <text x="400" y="300" font-family="Arial" font-size="24" fill="white" text-anchor="middle">ИГИИС - Цифровые решения</text>
  <text x="400" y="340" font-family="Arial" font-size="16" fill="white" text-anchor="middle">Изображение будет загружено</text>
</svg>''',
        
        'cropped-logo_IGIIS_-180x180.gif': '''<svg width="180" height="180" xmlns="http://www.w3.org/2000/svg">
  <circle cx="90" cy="90" r="80" fill="#478ac9"/>
  <text x="90" y="90" font-family="Arial" font-size="24" fill="white" text-anchor="middle" dy="8">ИГИИС</text>
</svg>'''
    }
    
    for filename, svg_content in placeholders.items():
        filepath = images_dir / filename.replace('.jpg', '.svg').replace('.gif', '.svg')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"  ✅ Создан placeholder: {filepath.name}")

def main():
    print("=" * 60)
    print("🔄 ИСПРАВЛЕНИЕ ПУТЕЙ К ИЗОБРАЖЕНИЯМ")
    print("=" * 60)
    
    # 1. Создаем placeholder изображения
    print("\n1. Создаю placeholder изображения...")
    create_placeholder_images()
    
    # 2. Исправляем CSS файлы
    print("\n2. Исправляю CSS файлы...")
    fix_css_images()
    
    # 3. Создаем упрощенную версию HomePage.css
    print("\n3. Создаю упрощенный CSS...")
    create_simple_css()
    
    print("\n" + "=" * 60)
    print("✅ ИСПРАВЛЕНИЯ ЗАВЕРШЕНЫ!")
    print("=" * 60)
    
    print("\n🚀 ДАЛЬНЕЙШИЕ ДЕЙСТВИЯ:")
    print("1. Обновите страницу в браузере (F5)")
    print("2. Если ошибки остались, запустите:")
    print("   cd frontend")
    print("   npm start -- --clear-cache")
    print("\n💡 ВАЖНО: Настоящие изображения нужно будет скопировать:")
    print("   Из original_files/images/ → frontend/src/assets/images/")

def create_simple_css():
    """Создает упрощенные версии CSS без проблемных изображений"""
    
    # Упрощенный HomePage.css
    homepage_css = Path("frontend/src/pages/public/HomePage.css")
    if homepage_css.exists():
        simple_css = '''/* Упрощенный HomePage.css - без проблемных изображений */
.HomePage-container {
  font-family: 'Open Sans', sans-serif;
}

.u-section-1 {
  min-height: 932px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  position: relative;
}

.u-section-1 .u-image-1 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  background-position: 50% 50%;
  min-height: 932px;
}

.u-section-1 .u-text-1 {
  font-weight: 700;
  font-size: 4.5rem;
  margin: 64px 30px 0;
  color: white;
}

.u-section-1 .u-list-1 {
  width: 1040px;
  margin: 249px 15px 0 auto;
}

.u-section-1 .u-repeater-1 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 30px;
  min-height: 472px;
}

.u-section-1 .u-list-item-1 {
  background: white;
  box-shadow: 5px 5px 20px 0 rgba(0,0,0,0.4);
  padding: 20px;
  border-radius: 8px;
}

.u-section-1 .u-icon-2 {
  height: 64px;
  width: 64px;
  background: #478ac9;
  border-radius: 50%;
  margin: 21px 131px 0 19px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.u-section-1 .u-text-2 {
  text-transform: uppercase;
  font-size: 1.25rem;
  letter-spacing: 1px;
  font-weight: 700;
  margin: 20px 19px 0;
}

.u-section-1 .u-btn-2 {
  border: 2px solid #478ac9;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.875rem;
  margin: 15px 0 0;
  padding: 10px 31px 10px 30px;
  background: white;
  color: #478ac9;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s;
}

.u-section-1 .u-btn-2:hover {
  background: #478ac9;
  color: white;
}

.u-section-1 .u-text-3 {
  margin: 23px 19px 0;
  color: #666;
}

/* Адаптивность */
@media (max-width: 1199px) {
  .u-section-1 {
    min-height: 802px;
  }
  
  .u-section-1 .u-image-1 {
    min-height: 768px;
  }
  
  .u-section-1 .u-text-1 {
    font-size: 4.0625rem;
  }
  
  .u-section-1 .u-list-1 {
    width: 470px;
  }
  
  .u-section-1 .u-repeater-1 {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 991px) {
  .u-section-1 {
    min-height: 615px;
  }
  
  .u-section-1 .u-image-1 {
    min-height: 588px;
  }
  
  .u-section-1 .u-text-1 {
    font-size: 3rem;
  }
  
  .u-section-1 .u-list-1 {
    width: 360px;
  }
}

@media (max-width: 767px) {
  .u-section-1 .u-repeater-1 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 575px) {
  .u-section-1 .u-repeater-1 {
    grid-template-columns: 1fr;
  }
}
'''
        with open(homepage_css, 'w', encoding='utf-8') as f:
            f.write(simple_css)
        print("  ✅ Создан упрощенный HomePage.css")

if __name__ == "__main__":
    main()# fix_image_paths.py
import os
import re
from pathlib import Path

def fix_css_images():
    print("🖼️ Исправляю пути к изображениям в CSS...")
    
    css_dir = Path("frontend/src/pages/public")
    
    # Находим все CSS файлы
    css_files = list(css_dir.glob("*.css"))
    
    for css_file in css_files:
        print(f"\n📄 Обрабатываю: {css_file.name}")
        
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Исправляем пути к изображениям
        # Было: url("/images/файл.jpg") 
        # Стало: url("/assets/images/файл.jpg") или убираем путь если файла нет
        
        # Вариант 1: Исправляем на правильный путь
        fixed_content = re.sub(
            r'url\("/images/([^"]+)"\)',
            r'url("/assets/images/\1")',
            content
        )
        
        # Вариант 2: Для теста можно заменить на простой цвет
        if 'background-image' in fixed_content:
            fixed_content = re.sub(
                r'background-image:\s*url\([^)]+\);',
                'background-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%);',
                fixed_content
            )
        
        # Сохраняем исправленный файл
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"  ✅ Исправлен: {css_file.name}")

def create_placeholder_images():
    """Создает placeholder изображения если реальных нет"""
    
    images_dir = Path("frontend/src/assets/images")
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Создаем простые SVG изображения как placeholder
    placeholders = {
        'global-business-internet-network-connection-iot-internet-things-business-intelligence-concept-busines-global-network-futuristic-technology-background-ai-generative.jpg': '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#667eea"/>
      <stop offset="100%" stop-color="#764ba2"/>
    </linearGradient>
  </defs>
  <rect width="800" height="600" fill="url(#grad1)"/>
  <text x="400" y="300" font-family="Arial" font-size="24" fill="white" text-anchor="middle">ИГИИС - Цифровые решения</text>
  <text x="400" y="340" font-family="Arial" font-size="16" fill="white" text-anchor="middle">Изображение будет загружено</text>
</svg>''',
        
        'cropped-logo_IGIIS_-180x180.gif': '''<svg width="180" height="180" xmlns="http://www.w3.org/2000/svg">
  <circle cx="90" cy="90" r="80" fill="#478ac9"/>
  <text x="90" y="90" font-family="Arial" font-size="24" fill="white" text-anchor="middle" dy="8">ИГИИС</text>
</svg>'''
    }
    
    for filename, svg_content in placeholders.items():
        filepath = images_dir / filename.replace('.jpg', '.svg').replace('.gif', '.svg')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"  ✅ Создан placeholder: {filepath.name}")

def main():
    print("=" * 60)
    print("🔄 ИСПРАВЛЕНИЕ ПУТЕЙ К ИЗОБРАЖЕНИЯМ")
    print("=" * 60)
    
    # 1. Создаем placeholder изображения
    print("\n1. Создаю placeholder изображения...")
    create_placeholder_images()
    
    # 2. Исправляем CSS файлы
    print("\n2. Исправляю CSS файлы...")
    fix_css_images()
    
    # 3. Создаем упрощенную версию HomePage.css
    print("\n3. Создаю упрощенный CSS...")
    create_simple_css()
    
    print("\n" + "=" * 60)
    print("✅ ИСПРАВЛЕНИЯ ЗАВЕРШЕНЫ!")
    print("=" * 60)
    
    print("\n🚀 ДАЛЬНЕЙШИЕ ДЕЙСТВИЯ:")
    print("1. Обновите страницу в браузере (F5)")
    print("2. Если ошибки остались, запустите:")
    print("   cd frontend")
    print("   npm start -- --clear-cache")
    print("\n💡 ВАЖНО: Настоящие изображения нужно будет скопировать:")
    print("   Из original_files/images/ → frontend/src/assets/images/")

def create_simple_css():
    """Создает упрощенные версии CSS без проблемных изображений"""
    
    # Упрощенный HomePage.css
    homepage_css = Path("frontend/src/pages/public/HomePage.css")
    if homepage_css.exists():
        simple_css = '''/* Упрощенный HomePage.css - без проблемных изображений */
.HomePage-container {
  font-family: 'Open Sans', sans-serif;
}

.u-section-1 {
  min-height: 932px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  position: relative;
}

.u-section-1 .u-image-1 {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  background-position: 50% 50%;
  min-height: 932px;
}

.u-section-1 .u-text-1 {
  font-weight: 700;
  font-size: 4.5rem;
  margin: 64px 30px 0;
  color: white;
}

.u-section-1 .u-list-1 {
  width: 1040px;
  margin: 249px 15px 0 auto;
}

.u-section-1 .u-repeater-1 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 30px;
  min-height: 472px;
}

.u-section-1 .u-list-item-1 {
  background: white;
  box-shadow: 5px 5px 20px 0 rgba(0,0,0,0.4);
  padding: 20px;
  border-radius: 8px;
}

.u-section-1 .u-icon-2 {
  height: 64px;
  width: 64px;
  background: #478ac9;
  border-radius: 50%;
  margin: 21px 131px 0 19px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.u-section-1 .u-text-2 {
  text-transform: uppercase;
  font-size: 1.25rem;
  letter-spacing: 1px;
  font-weight: 700;
  margin: 20px 19px 0;
}

.u-section-1 .u-btn-2 {
  border: 2px solid #478ac9;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.875rem;
  margin: 15px 0 0;
  padding: 10px 31px 10px 30px;
  background: white;
  color: #478ac9;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s;
}

.u-section-1 .u-btn-2:hover {
  background: #478ac9;
  color: white;
}

.u-section-1 .u-text-3 {
  margin: 23px 19px 0;
  color: #666;
}

/* Адаптивность */
@media (max-width: 1199px) {
  .u-section-1 {
    min-height: 802px;
  }
  
  .u-section-1 .u-image-1 {
    min-height: 768px;
  }
  
  .u-section-1 .u-text-1 {
    font-size: 4.0625rem;
  }
  
  .u-section-1 .u-list-1 {
    width: 470px;
  }
  
  .u-section-1 .u-repeater-1 {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 991px) {
  .u-section-1 {
    min-height: 615px;
  }
  
  .u-section-1 .u-image-1 {
    min-height: 588px;
  }
  
  .u-section-1 .u-text-1 {
    font-size: 3rem;
  }
  
  .u-section-1 .u-list-1 {
    width: 360px;
  }
}

@media (max-width: 767px) {
  .u-section-1 .u-repeater-1 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 575px) {
  .u-section-1 .u-repeater-1 {
    grid-template-columns: 1fr;
  }
}
'''
        with open(homepage_css, 'w', encoding='utf-8') as f:
            f.write(simple_css)
        print("  ✅ Создан упрощенный HomePage.css")

if __name__ == "__main__":
    main()