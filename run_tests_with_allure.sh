#!/bin/zsh
set -e

RUN_NAME=${1:-"run_$(date +%Y-%m-%d_%H-%M-%S)"}

echo "🔹 Run name: $RUN_NAME"

echo "🧹 Cleaning reports/allure-results..."
rm -rf reports/allure-results
mkdir -p reports/allure-results

# ---------- CATEGORIES ----------
if [ -f "reports/categories.json" ]; then
  echo "🏷  Copying categories.json to allure-results..."
  cp reports/categories.json reports/allure-results/categories.json
fi

# ---------- EXECUTOR JSON --------
echo "⚙️ Creating executor.json..."
cat > reports/allure-results/executor.json <<EOF
{
  "name": "Local Run",
  "type": "manual",
  "buildOrder": $(date +%s),
  "buildName": "${RUN_NAME}",
  "reportName": "${RUN_NAME}",
  "environment": "Local MacOS - Python 3.13",
  "executor": {
    "name": "Samuel",
    "type": "manual",
    "hostname": "Minas-Tirith"
  }
}
EOF

# ---------- HISTORY ----------
if [ -d "reports/allure-report/history" ]; then
  echo "📚 Copying previous history into new results..."
  mkdir -p reports/allure-results/history
  cp -R reports/allure-report/history/* reports/allure-results/history/
fi

# ---------- RUN TESTS ----------
echo "🧪 Running tests with pytest..."
set +e
pytest tests --alluredir=reports/allure-results
TEST_EXIT_CODE=$?
set -e

# ---------- GENERATE REPORT ----------
echo "📊 Generating Allure report..."
allure generate reports/allure-results -o reports/allure-report --clean

# ---------- ARCHIVE ----------
ARCHIVE_DIR="reports/archive/${RUN_NAME}"
echo "📦 Archiving report to ${ARCHIVE_DIR}..."
mkdir -p "${ARCHIVE_DIR}"
cp -R reports/allure-report "${ARCHIVE_DIR}/"

echo "✅ Done."
echo "👉 Last report: reports/allure-report"
echo "👉 Archived report: ${ARCHIVE_DIR}/allure-report"

exit $TEST_EXIT_CODE