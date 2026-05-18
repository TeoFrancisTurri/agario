#!/bin/bash
set -e

if ! command -v python3 &>/dev/null; then
    echo "Error: Python 3 no encontrado. Instalalo desde https://python.org"
    exit 1
fi

python3 -m venv venv
source venv/bin/activate
pip install --quiet -r requirements.txt

echo "Listo. Para ejecutar el cliente:"
echo "  source venv/bin/activate"
echo "  python -m client.main"
