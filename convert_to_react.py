import os
import re
import shutil
from pathlib import Path

def convert_html_to_jsx(html_content, component_name):
    """Конвертирует HTML в JSX с сохранением визуального отображения"""
    
    # 1. Удаляем ненужные теги
    html_content = re.sub(r'<!DOCTYPE[^>]*>', '', html_content)
    html_content = re.sub(r'<html[^>]*>|</html>', '', html_content)
    html_content = re.sub(r'<head>.*?</head>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<body[^>]*>|</body>', '', html_content)
    
    # 2. Заменяем HTML атрибуты на JSX (СОХРАНЯЯ ВИЗУАЛЬНЫЙ ВИД)
    replacements = [
        ('class="', 'className="'),      # Важно для CSS
        ('for="', 'htmlFor="'),          # Для label
    ]
    
    for old, new in replacements:
        html_content = html_content.replace(old, new)
    
    # 3. Обработка форм - сохраняем структуру, меняем отправку
    html_content = re.sub(
        r'<form([^>]*)action="[^"]*"([^>]*)>',
        r'<form\1\2 onSubmit={handleSubmit}>',
        html_content
    )
    
    # 4. Удаляем ненужные скрипты конструктора
    html_content = re.sub(
        r'<script[^>]*src="(jquery|nicepage)\.js"[^>]*>.*?</script>',
        '',
        html_content,
        flags=re.DOTALL
    )
    
    # 5. Заменяем inline стили на JSX формат
    def replace_style(match):
        style_content = match.group(1)
        # Простая замена кавычек для JSX
        return f'style={{{{ {style_content} }}}}'
    
    html_content = re.sub(
        r'style="([^"]*)"',
        replace_style,
        html_content
    )
    
    return html_content

def process_css_file(css_content, component_name):
    """Обрабатывает CSS файл для React"""
    
    # 1. Исправляем пути к изображениям
    css_content = re.sub(
        r'url\("/images/([^"]+)"\)',
        r'url("/assets/images/\1")',
        css_content
    )
    
    # 2. Удаляем CSS комментарии конструктора (если есть)
    css_content = re.sub(r'/\*.*?For immediate assistance.*?\*/', '', css_content, flags=re.DOTALL)
    
    return css_content

def create_react_component(html_content, component_name):
    """Создает полный React компонент"""
    
    return f'''import React, {{ useState }} from 'react';
import {{ useNavigate }} from 'react-router-dom';
import axios from 'axios';
import './{component_name}.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const {component_name} = () => {{
  const navigate = useNavigate();
  const [formData, setFormData] = useState({{}});
  const [loading, setLoading] = useState(false);
  
  // Обработчик изменения полей формы
  const handleInputChange = (e) => {{
    const {{ name, value, type, checked }} = e.target;
    setFormData(prev => ({{
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }}));
  }};
  
  // Обработчик отправки формы
  const handleSubmit = async (e) => {{
    e.preventDefault();
    setLoading(true);
    
    try {{
      // Определяем тип формы по component_name
      let endpoint = '';
      if ("{component_name}".includes('Density')) {{
        endpoint = '/calculations/density/';
      }} else if ("{component_name}".includes('Survey')) {{
        endpoint = '/survey/programs/';
      }} else {{
        endpoint = '/submissions/';
      }}
      
      const response = await axios.post(`${{API_URL}}${{endpoint}}`, formData);
      
      if (response.data.success) {{
        navigate('/thank-you', {{ 
          state: {{ 
            message: 'Данные успешно отправлены!',
            data: response.data 
          }}
        }});
      }}
    }} catch (error) {{
      console.error('Ошибка отправки:', error);
      alert('Ошибка при отправке данных. Пожалуйста, попробуйте снова.');
    }} finally {{
      setLoading(false);
    }}
  }};
  
  return (
    <>
{html_content}
    </>
  );
}};

export default {component_name};
'''

def main():
    print("🚀 Начинаем конвертацию HTML/CSS в React компоненты...")
    print("=" * 60)
    
    # Пути
    original_dir = Path("original_files")
    react_pages_dir = Path("stroycompany/frontend/src/pages/public")
    
    # Проверяем исходную папку
    if not original_dir.exists():
        print(f"❌ ОШИБКА: Папка '{original_dir}' не найдена!")
        print(f"Создайте папку 'original_files' в корне проекта и поместите туда:")
        print("  - Главная.html, Главная.css")
        print("  - Страница 2.html, Страница-2.css")
        print("  - Программа.html, Программа.css")
        print("  - Thank-You-Page-Template.html, Thank-You-Page-Template.css")
        return
    
    # Создаем целевую папку
    react_pages_dir.mkdir(parents=True, exist_ok=True)
    
    # Маппинг файлов на React компоненты
    file_mapping = {
        'Главная.html': 'HomePage',
        'Страница 2.html': 'DensityCalculation',
        'Программа.html': 'SurveyProgram',
        'Thank-You-Page-Template.html': 'ThankYouPage'
    }
    
    # Статистика
    converted_count = 0
    errors = []
    
    # Обрабатываем каждый HTML файл
    for html_filename, component_name in file_mapping.items():
        html_path = original_dir / html_filename
        css_filename = html_filename.replace('.html', '.css')
        css_path = original_dir / css_filename
        
        print(f"\n📄 Обрабатываем: {html_filename} → {component_name}")
        
        # Проверяем существование файлов
        if not html_path.exists():
            errors.append(f"HTML файл не найден: {html_filename}")
            continue
        
        if not css_path.exists():
            errors.append(f"CSS файл не найден: {css_filename}")
            continue
        
        try:
            # Читаем файлы
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            with open(css_path, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            # Конвертируем HTML в JSX
            jsx_content = convert_html_to_jsx(html_content, component_name)
            
            # Создаем React компонент
            react_component = create_react_component(jsx_content, component_name)
            
            # Сохраняем React компонент
            js_file = react_pages_dir / f"{component_name}.js"
            with open(js_file, 'w', encoding='utf-8') as f:
                f.write(react_component)
            
            # Обрабатываем и сохраняем CSS
            processed_css = process_css_file(css_content, component_name)
            css_file = react_pages_dir / f"{component_name}.css"
            with open(css_file, 'w', encoding='utf-8') as f:
                f.write(processed_css)
            
            print(f"  ✅ Создано: {component_name}.js")
            print(f"  ✅ Создано: {component_name}.css")
            converted_count += 1
            
        except Exception as e:
            errors.append(f"Ошибка при обработке {html_filename}: {str(e)}")
    
    # Создаем общий CSS файл с глобальными стилями
    print(f"\n🎨 Создаю глобальные стили...")
    global_css_path = Path("stroycompany/frontend/src/styles/global.css")
    global_css_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(global_css_path, 'w', encoding='utf-8') as f:
        f.write('''/* Глобальные стили для проекта ИГИИС */
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

/* Сохраняем стили конструктора Nicepage */
.u-body {
  font-size: 16px;
}

.u-xl-mode {
  /* Специфичные стили для режима конструктора */
}

/* Общие стили для форм */
form {
  margin: 20px 0;
}

input, select, textarea {
  font-family: inherit;
  font-size: inherit;
}

button {
  cursor: pointer;
}

/* Адаптивность */
@media (max-width: 768px) {
  body {
    font-size: 14px;
  }
}
''')
    print(f"  ✅ Создано: styles/global.css")
    
    # Обновляем App.js для маршрутизации
    print(f"\n🔄 Обновляю маршрутизацию...")
    
    # Создаем базовый App.js
    create_basic_app_js(file_mapping)
    
    print("\n" + "=" * 60)
    print("✅ КОНВЕРТАЦИЯ ЗАВЕРШЕНА!")
    print("=" * 60)
    
    # Вывод статистики
    print(f"\n📊 Статистика:")
    print(f"  Преобразовано страниц: {converted_count}/{len(file_mapping)}")
    
    if errors:
        print(f"\n⚠️  Обнаружены ошибки:")
        for error in errors:
            print(f"  - {error}")
    
    # Инструкции по дальнейшим действиям
    print(f"\n🚀 СЛЕДУЮЩИЕ ШАГИ:")
    print(f"1. Перейдите в папку фронтенда: cd stroycompany/frontend")
    print(f"2. Установите зависимости: npm install")
    print(f"3. Запустите React: npm start")
    print(f"4. Откройте браузер: http://localhost:3000")
    
    print(f"\n🔧 ЧТО ПРОВЕРИТЬ ПОСЛЕ ЗАПУСКА:")
    print(f"  • Внешний вид страниц (должен быть идентичен оригиналу)")
    print(f"  • Работа форм (пока будут выводиться в консоль)")
    print(f"  • Изображения (если есть проблемы с путями)")
    
    print(f"\n📁 СТРУКТУРА ПОСЛЕ КОНВЕРТАЦИИ:")
    print(f"stroycompany/frontend/src/pages/public/")
    for component_name in file_mapping.values():
        print(f"  ├── {component_name}.js    ← React компонент")
        print(f"  ├── {component_name}.css   ← Стили")
    
    print(f"\n💡 ДЛЯ СВЯЗИ С БАЗОЙ ДАННЫХ:")
    print(f"Пришлите структуру БД - я создам API эндпоинты в бэкенде!")

def create_basic_app_js(file_mapping):
    """Создает базовый App.js если он не существует"""
    
    # Создаем импорты
    imports = []
    for comp_name in file_mapping.values():
        imports.append(f"import {comp_name} from './pages/public/{comp_name}';")
    
    imports_section = '\n'.join(imports)
    
    # Создаем маршруты
    routes = []
    for comp_name in file_mapping.values():
        route_path = comp_name.lower()
        if comp_name == 'HomePage':
            route_path = '/'
        else:
            route_path = f'/{comp_name.lower()}'
        
        routes.append(f'          <Route path="{route_path}" element=<{comp_name} /> />')
    
    routes_section = '\n'.join(routes)
    
    app_js_content = f'''import React from 'react';
import {{ BrowserRouter as Router, Routes, Route }} from 'react-router-dom';
import './styles/global.css';

// Public pages
{imports_section}

function App() {{
  return (
    <Router>
      <div className="App">
        <Routes>
          {{/* Public routes */}}
{routes_section}
        </Routes>
      </div>
    </Router>
  );
}}

export default App;
'''
    
    app_js_path = Path("stroycompany/frontend/src/App.js")
    app_js_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(app_js_path, 'w', encoding='utf-8') as f:
        f.write(app_js_content)
    
    print(f"  ✅ Создан/обновлен: App.js с маршрутами")
    
    # Создаем index.js если его нет
    index_js_path = Path("stroycompany/frontend/src/index.js")
    if not index_js_path.exists():
        index_js_content = '''import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''
        index_js_path.parent.mkdir(parents=True, exist_ok=True)
        with open(index_js_path, 'w', encoding='utf-8') as f:
            f.write(index_js_content)
        
        print(f"  ✅ Создан: index.js")
    
    # Создаем package.json если его нет
    package_json_path = Path("stroycompany/frontend/package.json")
    if not package_json_path.exists():
        package_json_content = '''{
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
}
'''
        package_json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(package_json_path, 'w', encoding='utf-8') as f:
            f.write(package_json_content)
        
        print(f"  ✅ Создан: package.json")
    
    # Создаем public/index.html если его нет
    public_dir = Path("stroycompany/frontend/public")
    public_dir.mkdir(parents=True, exist_ok=True)
    
    index_html_path = public_dir / "index.html"
    if not index_html_path.exists():
        index_html_content = '''<!DOCTYPE html>
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
'''
        with open(index_html_path, 'w', encoding='utf-8') as f:
            f.write(index_html_content)
        
        print(f"  ✅ Создан: public/index.html")

if __name__ == "__main__":
    main()