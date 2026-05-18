@echo off

python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python no encontrado. Instalalo desde https://python.org
    exit /b 1
)

python -m venv venv
call venv\Scripts\activate
pip install --quiet -r requirements.txt

echo Listo. Para ejecutar el cliente:
echo   venv\Scripts\activate
echo   python -m client.main
