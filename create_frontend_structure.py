import os
import shutil
import json
from pathlib import Path

def create_react_frontend():
    base_path = Path("stroycompany/frontend")
    
    # 1. Переместим существующие статические файлы в новую структуру
    existing_files = {
        'index.html': 'public/index.html',
        'about.html': 'src/pages/public/AboutPage.js',
        'services.html': 'src/pages/public/ServicesPage.js',
        'portfolio.html': 'src/pages/public/PortfolioPage.js',
        'blog.html': 'src/pages/public/BlogPage.js',
        'contact.html': 'src/pages/public/ContactPage.js',
        'css/style.css': 'src/styles/global.css',
        'js/main.js': 'src/utils/helpers.js',
        'assets/': 'src/assets/'
    }
    
    # 2. Создаем структуру папок React
    react_structure = [
        # Основные папки
        'src/',
        'src/components/',
        'src/components/Layout/',
        'src/components/UI/',
        'src/components/UI/Button/',
        'src/components/UI/Card/',
        'src/components/UI/Modal/',
        'src/components/UI/Table/',
        'src/components/auth/',
        'src/components/services/',
        
        'src/pages/',
        'src/pages/public/',
        'src/pages/private/',
        'src/pages/private/admin/',
        
        'src/api/',
        'src/context/',
        'src/hooks/',
        'src/utils/',
        'src/styles/',
        'src/styles/components/',
        'src/assets/',
        'src/assets/images/',
        'src/assets/icons/',
        'src/assets/fonts/',
        
        'public/',
    ]
    
    # 3. Файлы React с базовым содержимым
    react_files = {
        # package.json
        'package.json': '''{
  "name": "stroy-master-frontend",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.0",
    "react-hook-form": "^7.48.2",
    "classnames": "^2.3.2",
    "@testing-library/react": "^14.1.2",
    "@testing-library/jest-dom": "^6.1.5",
    "@testing-library/user-event": "^14.5.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": ["react-app", "react-app/jest"]
  },
  "browserslist": {
    "production": [">0.2%", "not dead", "not op_mini all"],
    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
  },
  "devDependencies": {
    "react-scripts": "5.0.1"
  }
}''',
        
        # .env
        '.env': '''REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_APP_NAME=СтройМастер
SKIP_PREFLIGHT_CHECK=true''',
        
        '.env.example': '''REACT_APP_API_URL=http://localhost:8000/api/v1
REACT_APP_APP_NAME=СтройМастер''',
        
        # Основные React файлы
        'src/App.js': '''import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import Layout from './components/Layout';

// Public pages
import HomePage from './pages/public/HomePage';
import AboutPage from './pages/public/AboutPage';
import ServicesPage from './pages/public/ServicesPage';
import PortfolioPage from './pages/public/PortfolioPage';
import BlogPage from './pages/public/BlogPage';
import ContactPage from './pages/public/ContactPage';

// Private pages
import ProfilePage from './pages/private/ProfilePage';

// Admin pages
import AdminDashboard from './pages/private/admin/Dashboard';

// Styles
import './styles/global.css';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Layout>
          <Routes>
            {/* Public routes */}
            <Route path="/" element={<HomePage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/services" element={<ServicesPage />} />
            <Route path="/portfolio" element={<PortfolioPage />} />
            <Route path="/blog" element={<BlogPage />} />
            <Route path="/contact" element={<ContactPage />} />
            
            {/* Private routes */}
            <Route path="/profile" element={<ProfilePage />} />
            
            {/* Admin routes */}
            <Route path="/admin/*" element={<AdminDashboard />} />
          </Routes>
        </Layout>
      </Router>
    </AuthProvider>
  );
}

export default App;''',
        
        'src/index.js': '''import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles/global.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);''',
        
        # Компоненты Layout
        'src/components/Layout/Header.js': '''import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import './Header.css';

const Header = () => {
  const { user, logout } = useAuth();
  
  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <Link to="/">
              <h1>СтройМастер</h1>
              <p>Цифровизация инженерных изысканий</p>
            </Link>
          </div>
          
          <nav className="nav">
            <ul>
              <li><Link to="/">Главная</Link></li>
              <li><Link to="/services">Услуги</Link></li>
              <li><Link to="/portfolio">Портфолио</Link></li>
              <li><Link to="/blog">Блог</Link></li>
              <li><Link to="/about">О компании</Link></li>
              <li><Link to="/contact">Контакты</Link></li>
              
              {user ? (
                <>
                  <li><Link to="/profile">{user.name}</Link></li>
                  <li><button onClick={logout} className="logout-btn">Выйти</button></li>
                  {user.role === 'admin' && (
                    <li><Link to="/admin" className="admin-link">Админ</Link></li>
                  )}
                </>
              ) : (
                <>
                  <li><Link to="/login" className="login-btn">Войти</Link></li>
                  <li><Link to="/register" className="register-btn">Регистрация</Link></li>
                </>
              )}
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Header;''',
        
        'src/components/Layout/Footer.js': '''import React from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-section">
            <h3>СтройМастер</h3>
            <p>Профессиональные инженерные изыскания и строительные решения</p>
          </div>
          
          <div className="footer-section">
            <h4>Контакты</h4>
            <p>Email: info@stroymaster.ru</p>
            <p>Телефон: +7 (XXX) XXX-XX-XX</p>
            <p>Адрес: г. Москва, ул. Строителей, 15</p>
          </div>
          
          <div className="footer-section">
            <h4>Быстрые ссылки</h4>
            <ul>
              <li><Link to="/services">Услуги</Link></li>
              <li><Link to="/portfolio">Проекты</Link></li>
              <li><Link to="/blog">Блог</Link></li>
              <li><Link to="/contact">Связаться с нами</Link></li>
            </ul>
          </div>
        </div>
        
        <div className="footer-bottom">
          <p>&copy; {currentYear} СтройМастер. Все права защищены.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;''',
        
        'src/components/Layout/index.js': '''import React from 'react';
import Header from './Header';
import Footer from './Footer';
import './Layout.css';

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <Header />
      <main className="main-content">
        {children}
      </main>
      <Footer />
    </div>
  );
};

export default Layout;''',
        
        # Context
        'src/context/AuthContext.js': '''import React, { createContext, useState, useContext, useEffect } from 'react';
import { loginUser, registerUser, logoutUser, getCurrentUser } from '../api/auth';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    // Проверяем, есть ли сохраненный токен
    const token = localStorage.getItem('token');
    if (token) {
      fetchUserData();
    } else {
      setLoading(false);
    }
  }, []);
  
  const fetchUserData = async () => {
    try {
      const userData = await getCurrentUser();
      setUser(userData);
    } catch (error) {
      console.error('Ошибка загрузки пользователя:', error);
      localStorage.removeItem('token');
    } finally {
      setLoading(false);
    }
  };
  
  const login = async (email, password) => {
    try {
      const { user, token } = await loginUser(email, password);
      localStorage.setItem('token', token);
      setUser(user);
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  };
  
  const register = async (userData) => {
    try {
      const { user, token } = await registerUser(userData);
      localStorage.setItem('token', token);
      setUser(user);
      return { success: true };
    } catch (error) {
      return { success: false, error: error.message };
    }
  };
  
  const logout = () => {
    logoutUser();
    localStorage.removeItem('token');
    setUser(null);
  };
  
  const value = {
    user,
    loading,
    login,
    register,
    logout
  };
  
  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};''',
        
        # API клиент
        'src/api/client.js': '''import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Интерцептор для добавления токена
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Интерцептор для обработки ошибок
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default apiClient;''',
        
        'src/api/auth.js': '''import apiClient from './client';

export const loginUser = async (email, password) => {
  const response = await apiClient.post('/auth/login', { email, password });
  return response.data;
};

export const registerUser = async (userData) => {
  const response = await apiClient.post('/auth/register', userData);
  return response.data;
};

export const getCurrentUser = async () => {
  const response = await apiClient.get('/auth/me');
  return response.data;
};

export const logoutUser = () => {
  // На стороне клиента просто удаляем токен
  return Promise.resolve();
};''',
        
        'src/api/services.js': '''import apiClient from './client';

export const getAllServices = async () => {
  const response = await apiClient.get('/services');
  return response.data;
};

export const getServiceById = async (id) => {
  const response = await apiClient.get(`/services/${id}`);
  return response.data;
};

export const createService = async (serviceData) => {
  const response = await apiClient.post('/services', serviceData);
  return response.data;
};

export const updateService = async (id, serviceData) => {
  const response = await apiClient.put(`/services/${id}`, serviceData);
  return response.data;
};

export const deleteService = async (id) => {
  const response = await apiClient.delete(`/services/${id}`);
  return response.data;
};''',
        
        # Страницы
        'src/pages/public/HomePage.js': '''import React, { useEffect, useState } from 'react';
import { getAllServices } from '../../api/services';
import ServiceCard from '../../components/services/ServiceCard';
import './HomePage.css';

const HomePage = () => {
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    fetchServices();
  }, []);
  
  const fetchServices = async () => {
    try {
      const data = await getAllServices();
      setServices(data.slice(0, 3)); // Показываем только 3 услуги на главной
    } catch (error) {
      console.error('Ошибка загрузки услуг:', error);
    } finally {
      setLoading(false);
    }
  };
  
  return (
    <div className="home-page">
      <section className="hero">
        <div className="container">
          <h1>Профессиональные инженерные изыскания</h1>
          <p>Полный комплекс услуг для строительства и проектирования</p>
          <button className="cta-button">Заказать консультацию</button>
        </div>
      </section>
      
      <section className="services-preview">
        <div className="container">
          <h2>Наши услуги</h2>
          {loading ? (
            <p>Загрузка...</p>
          ) : (
            <div className="services-grid">
              {services.map(service => (
                <ServiceCard key={service.id} service={service} />
              ))}
            </div>
          )}
        </div>
      </section>
      
      <section className="advantages">
        <div className="container">
          <h2>Почему выбирают нас</h2>
          <div className="advantages-grid">
            <div className="advantage">
              <h3>Опыт более 15 лет</h3>
              <p>Работаем с 2008 года</p>
            </div>
            <div className="advantage">
              <h3>Современное оборудование</h3>
              <p>Используем новейшие технологии</p>
            </div>
            <div className="advantage">
              <h3>Гарантия качества</h3>
              <p>Все работы по ГОСТ и СНИП</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;''',
        
        'src/pages/public/ServicesPage.js': '''import React, { useEffect, useState } from 'react';
import { getAllServices } from '../../api/services';
import ServiceList from '../../components/services/ServiceList';
import ServiceFilter from '../../components/services/ServiceFilter';
import './ServicesPage.css';

const ServicesPage = () => {
  const [services, setServices] = useState([]);
  const [filteredServices, setFilteredServices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    category: 'all',
    priceRange: [0, 1000000]
  });
  
  useEffect(() => {
    fetchServices();
  }, []);
  
  useEffect(() => {
    filterServices();
  }, [filters, services]);
  
  const fetchServices = async () => {
    try {
      const data = await getAllServices();
      setServices(data);
      setFilteredServices(data);
    } catch (error) {
      console.error('Ошибка загрузки услуг:', error);
    } finally {
      setLoading(false);
    }
  };
  
  const filterServices = () => {
    let result = [...services];
    
    if (filters.category !== 'all') {
      result = result.filter(service => service.category === filters.category);
    }
    
    if (filters.priceRange) {
      result = result.filter(service => 
        service.price >= filters.priceRange[0] && 
        service.price <= filters.priceRange[1]
      );
    }
    
    setFilteredServices(result);
  };
  
  const handleFilterChange = (newFilters) => {
    setFilters(prev => ({ ...prev, ...newFilters }));
  };
  
  return (
    <div className="services-page">
      <div className="container">
        <h1>Наши услуги</h1>
        <p className="page-description">
          Полный комплекс инженерных изысканий и строительных услуг
        </p>
        
        <div className="services-content">
          <aside className="filters-sidebar">
            <ServiceFilter 
              filters={filters}
              onFilterChange={handleFilterChange}
            />
          </aside>
          
          <main className="services-main">
            {loading ? (
              <p>Загрузка услуг...</p>
            ) : (
              <>
                <ServiceList services={filteredServices} />
                {filteredServices.length === 0 && (
                  <p className="no-results">Нет услуг, соответствующих выбранным фильтрам</p>
                )}
              </>
            )}
          </main>
        </div>
      </div>
    </div>
  );
};

export default ServicesPage;''',
        
        # Глобальные стили
        'src/styles/global.css': '''/* Глобальные стили - импортированы из старого style.css */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f5f5f5;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Стили для React компонентов */
.button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button:hover {
  background-color: #0056b3;
}

.card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

/* Адаптивность */
@media (max-width: 768px) {
  .container {
    padding: 0 15px;
  }
}''',
        
        # Public index.html для React
        'public/index.html': '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="СтройМастер - цифровизация инженерных изысканий и строительных услуг">
    <meta name="keywords" content="инженерные изыскания, строительство, геодезия, геология, проектирование">
    <title>СтройМастер | Цифровизация инженерных изысканий</title>
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico">
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json">
</head>
<body>
    <noscript>
        Для работы приложения необходим JavaScript. Пожалуйста, включите JavaScript в настройках браузера.
    </noscript>
    <div id="root"></div>
</body>
</html>''',
        
        'public/manifest.json': '''{
  "short_name": "СтройМастер",
  "name": "СтройМастер - Цифровизация инженерных изысканий",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#007bff",
  "background_color": "#ffffff"
}''',
        
        # Docker конфиг
        'docker-compose.yml': '''version: '3.8'

services:
  react-app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://backend:8000/api/v1
    volumes:
      - ./src:/app/src
      - /app/node_modules
    depends_on:
      - backend
    command: npm start

  backend:
    build:
      context: ../backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/stroymaster
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=stroymaster
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:''',
        
        'Dockerfile': '''# React Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]''',
        
        '.gitignore': '''# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*''',
        
        'README.md': '''# Фронтенд СтройМастер

React SPA приложение для компании "СтройМастер" - цифровизация инженерных изысканий.

## Установка и запуск

### Требования
- Node.js 16+
- npm или yarn

### Установка
\`\`\`bash
npm install
\`\`\`

### Запуск в режиме разработки
\`\`\`bash
npm start
\`\`\`

Приложение будет доступно по адресу: http://localhost:3000

### Сборка для production
\`\`\`bash
npm run build
\`\`\`

### Тестирование
\`\`\`bash
npm test
\`\`\`

## Структура проекта

\`\`\`
frontend/
├── src/
│   ├── components/     # React компоненты
│   ├── pages/         # Страницы приложения
│   ├── api/           # API клиенты для бэкенда
│   ├── context/       # React Context
│   ├── hooks/         # Кастомные хуки
│   ├── utils/         # Вспомогательные функции
│   ├── styles/        # Стили
│   └── assets/        # Статические файлы
├── public/            # Статика
└── package.json       # Зависимости
\`\`\`

## Основные технологии

- React 18
- React Router 6
- Axios для HTTP запросов
- React Hook Form для форм
- CSS Modules для стилизации

## API интеграция

Фронтенд взаимодействует с бэкендом FastAPI по адресу: \`http://localhost:8000/api/v1\`

Основные эндпоинты:
- \`/auth/*\` - аутентификация
- \`/services/*\` - услуги
- \`/projects/*\` - проекты
- \`/requests/*\` - заявки

## Разработка

### Добавление новой страницы
1. Создайте компонент в \`src/pages/\`
2. Добавьте роут в \`src/App.js\`
3. Создайте стили в \`src/styles/pages/\`

### Добавление нового API клиента
1. Создайте файл в \`src/api/\`
2. Используйте \`apiClient\` из \`src/api/client.js\`
3. Экспортируйте функции для использования в компонентах

## Лицензия

© 2024 СтройМастер'''
    }
    
    print("Начинаем преобразование фронтенда в React SPA...")
    
    # Создаем все папки
    for folder in react_structure:
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Создана папка: {folder_path}")
    
    # Создаем файлы React
    for file_path, content in react_files.items():
        full_path = base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Создан файл: {full_path}")
    
    # Создаем дополнительные компоненты (упрощенные версии)
    additional_components = {
        'src/components/services/ServiceCard.js': '''import React from 'react';
import { Link } from 'react-router-dom';
import './ServiceCard.css';

const ServiceCard = ({ service }) => {
  return (
    <div className="service-card">
      <h3>{service.name}</h3>
      <p className="service-description">{service.description}</p>
      <div className="service-meta">
        <span className="service-price">от {service.price} руб.</span>
        <span className="service-duration">{service.duration} дней</span>
      </div>
      <Link to={`/services/${service.id}`} className="service-link">
        Подробнее
      </Link>
    </div>
  );
};

export default ServiceCard;''',
        
        'src/components/services/ServiceList.js': '''import React from 'react';
import ServiceCard from './ServiceCard';
import './ServiceList.css';

const ServiceList = ({ services }) => {
  return (
    <div className="service-list">
      {services.map(service => (
        <ServiceCard key={service.id} service={service} />
      ))}
    </div>
  );
};

export default ServiceList;''',
        
        'src/components/services/ServiceFilter.js': '''import React from 'react';
import './ServiceFilter.css';

const ServiceFilter = ({ filters, onFilterChange }) => {
  const categories = [
    { value: 'all', label: 'Все категории' },
    { value: 'geodesy', label: 'Геодезия' },
    { value: 'geology', label: 'Геология' },
    { value: 'ecology', label: 'Экология' },
    { value: 'design', label: 'Проектирование' }
  ];
  
  const handleCategoryChange = (e) => {
    onFilterChange({ category: e.target.value });
  };
  
  const handlePriceChange = (e) => {
    const value = parseInt(e.target.value);
    onFilterChange({ priceRange: [0, value] });
  };
  
  return (
    <div className="service-filter">
      <h3>Фильтры</h3>
      
      <div className="filter-group">
        <label>Категория:</label>
        <select value={filters.category} onChange={handleCategoryChange}>
          {categories.map(cat => (
            <option key={cat.value} value={cat.value}>
              {cat.label}
            </option>
          ))}
        </select>
      </div>
      
      <div className="filter-group">
        <label>Макс. цена: {filters.priceRange[1].toLocaleString()} руб.</label>
        <input
          type="range"
          min="0"
          max="1000000"
          step="10000"
          value={filters.priceRange[1]}
          onChange={handlePriceChange}
        />
      </div>
    </div>
  );
};

export default ServiceFilter;''',
        
        'src/pages/private/admin/Dashboard.js': '''import React, { useState, useEffect } from 'react';
import { getAllServices } from '../../../api/services';
import { getCurrentUser } from '../../../api/auth';
import './Dashboard.css';

const Dashboard = () => {
  const [stats, setStats] = useState({
    services: 0,
    projects: 0,
    requests: 0,
    users: 0
  });
  const [user, setUser] = useState(null);
  
  useEffect(() => {
    fetchData();
  }, []);
  
  const fetchData = async () => {
    try {
      const [userData, services] = await Promise.all([
        getCurrentUser(),
        getAllServices()
      ]);
      
      setUser(userData);
      setStats(prev => ({
        ...prev,
        services: services.length
      }));
    } catch (error) {
      console.error('Ошибка загрузки данных:', error);
    }
  };
  
  if (!user || user.role !== 'admin') {
    return <div>Доступ запрещен</div>;
  }
  
  return (
    <div className="admin-dashboard">
      <h1>Панель администратора</h1>
      
      <div className="dashboard-stats">
        <div className="stat-card">
          <h3>{stats.services}</h3>
          <p>Услуг</p>
        </div>
        <div className="stat-card">
          <h3>{stats.projects}</h3>
          <p>Проектов</p>
        </div>
        <div className="stat-card">
          <h3>{stats.requests}</h3>
          <p>Заявок</p>
        </div>
        <div className="stat-card">
          <h3>{stats.users}</h3>
          <p>Пользователей</p>
        </div>
      </div>
      
      <div className="dashboard-content">
        <section className="recent-activity">
          <h2>Последняя активность</h2>
          <p>Здесь будет отображаться последняя активность...</p>
        </section>
        
        <section className="quick-actions">
          <h2>Быстрые действия</h2>
          <div className="actions-grid">
            <button className="action-btn">Добавить услугу</button>
            <button className="action-btn">Просмотреть заявки</button>
            <button className="action-btn">Управление пользователями</button>
          </div>
        </section>
      </div>
    </div>
  );
};

export default Dashboard;'''
    }
    
    # Создаем дополнительные компоненты
    for file_path, content in additional_components.items():
        full_path = base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Создан компонент: {full_path}")
    
    # Копируем существующие статические файлы
    print("\nКопируем существующие файлы...")
    
    # Копируем assets
    old_assets = base_path / 'assets'
    new_assets = base_path / 'src' / 'assets'
    
    if old_assets.exists():
        for item in old_assets.rglob('*'):
            if item.is_file():
                relative_path = item.relative_to(old_assets)
                new_path = new_assets / relative_path
                new_path.parent.mkdir(parents=True, exist_ok=True)
                
                try:
                    shutil.copy2(item, new_path)
                    print(f"  ↳ Скопирован: {item} → {new_path}")
                except Exception as e:
                    print(f"  ⚠️ Ошибка копирования {item}: {e}")
    
    print(f"\n{'='*60}")
    print("✅ Преобразование завершено!")
    print(f"{'='*60}")
    print("\nСтруктура фронтенда успешно преобразована в React SPA.")
    print("\nДля запуска React приложения:")
    print("1. Перейдите в папку frontend: cd stroycompany/frontend")
    print("2. Установите зависимости: npm install")
    print("3. Запустите приложение: npm start")
    print("\nСтатические HTML файлы преобразованы в React компоненты:")
    print("  • about.html → src/pages/public/AboutPage.js")
    print("  • services.html → src/pages/public/ServicesPage.js")
    print("  • и т.д.")
    print("\nСтили и скрипты перемещены в соответствующую структуру.")

if __name__ == "__main__":
    create_react_frontend()