#!/usr/bin/env bash
set -euo pipefail

echo "=== Установка ctl-app ==="

# Проверяем python3
if ! command -v python3 &>/dev/null; then
  echo "Ошибка: python3 не найден. Установите Python 3.7+." >&2
  exit 1
fi

# Создаём venv
echo "Создаём виртуальное окружение .venv..."
python3 -m venv .venv

# Активируем его
source .venv/bin/activate

# Обновляем pip и ставим пакет
echo "Обновляем pip и устанавливаем ctl-app..."
pip install --upgrade pip
pip install .

echo ""
echo "Успешно установлено! Команда 'ctl' доступна в виртуальном окружении."
echo "Для начала работы:"
echo "  source .venv/bin/activate"
echo "  ctl --help"
