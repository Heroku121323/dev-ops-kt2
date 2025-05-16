#!/usr/bin/env bash
set -euo pipefail

# Аргумент — тип апдейта: feature → minor, hotfix → patch
TYPE="$1"
case "$TYPE" in
  feature) UPDATE="minor" ;;
  hotfix)  UPDATE="patch" ;;
  *)
    echo "Usage: $0 <feature|hotfix>"
    exit 1
    ;;
esac

# Читаем старую версию
OLD_VERSION=$(<version)

# Парсим мажор, минор, патч
IFS='.' read -r MAJOR MINOR PATCH <<<"$OLD_VERSION"

# Бампим
if [[ "$UPDATE" == "minor" ]]; then
  MINOR=$((MINOR + 1))
  PATCH=0
else
  PATCH=$((PATCH + 1))
fi

NEW_VERSION="$MAJOR.$MINOR.$PATCH"

# Записываем новую версию
echo "$NEW_VERSION" > version

# Выводим для последующих шагов
echo "::set-output name=old::$OLD_VERSION"
echo "::set-output name=new::$NEW_VERSION"
echo "::set-output name=type::$UPDATE"
