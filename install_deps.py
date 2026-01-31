import subprocess
import sys

def install_packages():
    packages = [
        "fastapi==0.104.1",
        "uvicorn[standard]==0.24.0", 
        "sqlalchemy==2.0.23",
        "python-dotenv==1.0.0",
        "pydantic==2.5.0"
    ]
    
    print("Устанавливаем основные зависимости...")
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    print("\nПытаемся установить psycopg2...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psycopg2==2.9.9"])
        print("✅ psycopg2 успешно установлен")
    except:
        print("⚠️  psycopg2 не установился. Пробуем psycopg2-binary...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "psycopg2-binary==2.9.9"])
            print("✅ psycopg2-binary успешно установлен")
        except:
            print("❌ Оба варианта не работают. Используем SQLite для тестирования.")
            print("   Установите PostgreSQL или используйте SQLite.")

if __name__ == "__main__":
    install_packages()