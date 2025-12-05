#!/bin/zsh
set -e

# Nom du run (pour l'archive) : argument ou timestamp par défaut
RUN_NAME=${1:-"run_$(date +%Y-%m-%d_%H-%M-%S)"}

echo "🔹 Run name: $RUN_NAME"

# 1) Nettoyer les anciens résultats
echo "🧹 Cleaning reports/allure-results..."
rm -rf reports/allure-results
mkdir -p reports/allure-results

# 2) Ajouter les catégories Allure si le fichier existe
if [ -f "reports/categories.json" ]; then
  echo "🏷  Copying categories.json to allure-results..."
  cp reports/categories.json reports/allure-results/categories.json
fi

# 3) Si un rapport précédent existe, récupérer son historique pour le trend
if [ -d "reports/allure-report/history" ]; then
  echo "📚 Copying previous history into new results..."
  mkdir -p reports/allure-results/history
  cp -R reports/allure-report/history/* reports/allure-results/history/
fi

# 4) Lancer pytest avec génération des résultats Allure
echo "🧪 Running tests with pytest..."

set +e
pytest tests --alluredir=reports/allure-results
TEST_EXIT_CODE=$?
set -e

# 5) Générer le nouveau rapport Allure (avec historique et catégories)
echo "📊 Generating Allure report..."
allure generate reports/allure-results -o reports/allure-report --clean

# 6) Archiver ce rapport pour garder une trace
ARCHIVE_DIR="reports/archive/${RUN_NAME}"
echo "📦 Archiving report to ${ARCHIVE_DIR}..."
mkdir -p "${ARCHIVE_DIR}"
cp -R reports/allure-report "${ARCHIVE_DIR}/"

echo "✅ Done."
echo "👉 Last report: reports/allure-report"
echo "👉 Archived report: ${ARCHIVE_DIR}/allure-report"

exit $TEST_EXIT_CODE