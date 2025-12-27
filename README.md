# saucedemo-auth-automation

Login automation and testing project for [SauceDemo](https://www.saucedemo.com/).
Demonstrates modern Python test automation practices using **Playwright**, **Pytest**, **Page Object Model**, and **Allure**.

---

## Quick Start / Короткая инструкция

### Prerequisites / Требования
- **Python 3.10+**
- **uv** (recommended) or **pip**
- **Docker** (optional)
- **Make** (optional, for convenience)

### 1. Local Run / Локальный запуск

**Using Make (Recommended):**
```bash
# Install dependencies / Установка зависимостей
make install

# Run tests / Запуск тестов
make test

# Generate & Open Report / Открыть отчет
make report
```

**Using uv directly:**
```bash
uv sync
uv run playwright install --with-deps chromium
uv run pytest
# Generate and open Allure report:
allure generate allure-results -o allure-report --clean
allure open allure-report
```

**Using pip directly:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install --with-deps chromium
pytest
# Generate and open Allure report:
allure generate allure-results -o allure-report --clean
allure open allure-report
```

### 2. Docker Run / Запуск в Docker

```bash
# Build image / Сборка образа
make docker-build

# Run tests & Serve report / Запуск тестов и отчета
make docker-test
# If port 8080 is busy / Если порт 8080 занят:
# make docker-test PORT=8081
```
*Report will be available at http://localhost:8080 (or your custom port)*

---

## Tech Stack

- **Language**: Python 3.10
- **Browser Automation**: Playwright
- **Testing Framework**: Pytest
- **Reporting**: Allure Report
- **Package Manager**: uv
- **Containerization**: Docker

## Test Scenarios

1. **Successful Login**: `standard_user`
2. **Invalid Password**: Error handling check
3. **Locked Out User**: `locked_out_user` error check
4. **Empty Fields**: Validation check
5. **Performance Glitch**: `performance_glitch_user` navigation check

## Project Structure

```
saucedemo-auth-automation/
├── src/
│   └── pages/              # Page Object Models
├── tests/                  # Test scenarios
├── allure-results/         # Raw test results
├── allure-report/          # HTML report
├── Dockerfile              # Docker configuration
├── Makefile                # Command shortcuts
├── requirements.txt        # Dependencies (pip)
└── pyproject.toml          # Dependencies (uv)
```

## Detailed Instructions

### Installation (Manual)

If you don't have `make` or `uv`:

1.  **Install uv**:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2.  **Install dependencies**:
    ```bash
    uv sync
    uv run playwright install chromium
    ```

### Running Tests

- **Headless (default)**: `uv run pytest`
- **Headed (visible)**: `uv run pytest --headed`
- **Specific test**: `uv run pytest tests/test_login.py`

### Docker

The Docker container runs the tests and then starts a web server for the Allure report.
```bash
docker build -t saucedemo-auth-automation .
docker run --rm -it -p 8080:8080 saucedemo-auth-automation:latest
```
