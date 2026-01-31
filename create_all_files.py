import os
from pathlib import Path

def create_frontend_files():
    """Создает все фронтенд файлы"""
    base_path = Path("frontend/src/pages/public")
    base_path.mkdir(parents=True, exist_ok=True)
    
    # 1. HomePage.js
    home_js = base_path / "HomePage.js"
    home_js.write_text('''import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './HomePage.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

const HomePage = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const handleNavigation = (page) => {
    switch(page) {
      case 'survey':
        navigate('/survey');
        break;
      case 'density':
        navigate('/density');
        break;
      default:
        navigate('/');
    }
  };

  return (
    <section className="u-section-1">
      <div className="u-layout-wrap-1">
        <div className="u-image-1">
          <div className="u-container-layout-1">
            <h1 className="u-text-1">ИГИИС<br />
              <span style={{ fontSize: '3.75rem' }}>цифровые решения</span>
            </h1>
            
            <div className="u-list-1">
              <div className="u-repeater-1">
                {/* Карточка 1 */}
                <div className="u-list-item-1">
                  <div className="u-container-layout-2">
                    <span className="u-icon-2">
                      <img src="/assets/images/free-icon-homework-8577094.png" alt="Задание" />
                    </span>
                    <h4 className="u-text-2">ЗАДАНИЕ</h4>
                    <button className="u-btn-2" onClick={() => handleNavigation('assignment')}>
                      Сформировать
                    </button>
                    <p className="u-text-3">
                      Сервис формирования задания
                    </p>
                  </div>
                </div>
                
                {/* Карточка 2 */}
                <div className="u-list-item-2">
                  <div className="u-container-layout-3">
                    <span className="u-icon-3">
                      <img src="/assets/images/checklist.png" alt="Программа" />
                    </span>
                    <h4 className="u-text-4">ПРОГРАММА</h4>
                    <button className="u-btn-3" onClick={() => handleNavigation('survey')}>
                      Сформировать
                    </button>
                    <p className="u-text-5">
                      Формирование программы
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HomePage;''', encoding='utf-8')
    
    print(f"✓ Создан: {home_js}")
    
    # 2. Создайте остальные файлы по аналогии...
    
    # 3. Создайте папку для изображений
    images_path = Path("frontend/src/assets/images")
    images_path.mkdir(parents=True, exist_ok=True)
    print(f"✓ Создана папка для изображений: {images_path}")

def create_backend_files():
    """Создает все бэкенд файлы"""
    api_path = Path("backend/app/api/v1")
    api_path.mkdir(parents=True, exist_ok=True)
    
    # 1. calculations.py
    calc_py = api_path / "calculations.py"
    calc_py.write_text('''from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.calculation import DensityCalculation
from app.schemas.calculation import DensityCalculationCreate, DensityCalculationOut

router = APIRouter()

@router.post("/density/", response_model=DensityCalculationOut)
def create_density_calculation(
    calculation: DensityCalculationCreate,
    db: Session = Depends(get_db)
):
    """Создать расчет плотности"""
    db_calculation = DensityCalculation(**calculation.dict())
    db.add(db_calculation)
    db.commit()
    db.refresh(db_calculation)
    return db_calculation

@router.get("/density/", response_model=List[DensityCalculationOut])
def get_density_calculations(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Получить все расчеты плотности"""
    calculations = db.query(DensityCalculation).offset(skip).limit(limit).all()
    return calculations''', encoding='utf-8')
    
    print(f"✓ Создан: {calc_py}")
    
    # 2. survey.py
    survey_py = api_path / "survey.py"
    survey_py.write_text('''from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.survey import SurveyProgram
from app.schemas.survey import SurveyProgramCreate, SurveyProgramOut

router = APIRouter()

@router.post("/programs/", response_model=SurveyProgramOut)
def create_survey_program(
    program: SurveyProgramCreate,
    db: Session = Depends(get_db)
):
    """Создать программу изысканий"""
    db_program = SurveyProgram(**program.dict())
    db.add(db_program)
    db.commit()
    db.refresh(db_program)
    return db_program

@router.get("/programs/", response_model=List[SurveyProgramOut])
def get_survey_programs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Получить все программы изысканий"""
    programs = db.query(SurveyProgram).offset(skip).limit(limit).all()
    return programs''', encoding='utf-8')
    
    print(f"✓ Создан: {survey_py}")

def main():
    print("📁 Создаю все необходимые файлы...")
    print("=" * 60)
    
    create_frontend_files()
    print("-" * 40)
    create_backend_files()
    
    print("\n" + "=" * 60)
    print("✅ ВСЕ ФАЙЛЫ СОЗДАНЫ!")
    print("=" * 60)
    
    print("\n📋 ЧТО ДЕЛАТЬ ДАЛЬШЕ:")
    print("1. Скопируйте ваши изображения в:")
    print("   C:\\Projects\\stroycompany\\frontend\\src\\assets\\images\\")
    print("\n2. Запустите фронтенд:")
    print("   cd C:\\Projects\\stroycompany\\frontend")
    print("   npm start")
    print("\n3. Запустите бэкенд:")
    print("   cd C:\\Projects\\stroycompany\\backend")
    print("   python -m uvicorn app.main:app --reload --port 8000")

if __name__ == "__main__":
    main()