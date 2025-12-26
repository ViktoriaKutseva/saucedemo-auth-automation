# saucedemo-auth-automation
Login automation and testing project for SauceDemo
https://trace.playwright.dev/
This project automates testing of the login functionality for [SauceDemo](https://www.saucedemo.com/), a demo e-commerce website. It demonstrates modern Python test automation practices using the Page Object Model pattern.

It containts:

- **5 comprehensive login test scenarios**
- **Page Object Model** for maintainable code
- **Playwright** for reliable browser automation
- **Pytest** for powerful test organization
- **Allure Report** for beautiful test reporting
- **Docker** for consistent test environment
- **Type hints** for code clarity
- **Comprehensive documentation**

## Tech stack:

- **Python**: 3.10
- **Browser Automation**: Playwright
- **Testing Framework**: pytest
- **Reporting**: Allure Report
- **Package Manager**: uv (modern Python package manager)
- **Containerization**: Docker

## Project Structure


saucedemo-auth-automation/
├── src/
│   └── pages/              # Page Object Models
│       ├── base_page.py    # Base page with common functionality
│       ├── login_page.py   # Login page object
│       └── inventory_page.py # Inventory page object
├── tests/
│   ├── conftest.py         # Pytest fixtures
│   └── test_login.py       # Login test scenarios
├── allure-results/         # Test results (generated)
├── allure-report/          # HTML reports (generated)
├── pyproject.toml          # Project dependencies (uv)
├── requirements.txt        # Traditional requirements file
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Docker Compose configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file

## Prerequisites

- **Python 3.10** or higher
- **uv** package manager (or pip)
- **Docker** (optional, for containerized execution)
- **Allure command-line tool** (for report generation)
- **Java 8+** (required by Allure)

## Setup Instructions

### Option 1: Using uv (Recommended)


1. **Install uv**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Clone the repository**:
```bash
git clone <your-repo-url>
cd saucedemo-auth-automation
```

3. **Install dependencies**:
```bash
uv sync
```

4. **Install Playwright browsers**:
```bash
uv run playwright install chromium
```

5. **Install Allure** (if not already installed):
```bash
# macOS
brew install allure

# Ubuntu/Debian
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

### Option 2: Using pip

1. **Clone the repository**:
```bash
git clone <your-repo-url>
cd saucedemo-auth-automation
```

2. **Create virtual environment**:
```bash
python3.10 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**:
```bash
playwright install chromium
```

## Running Tests

### Run All Tests
```bash
# Using uv
uv run pytest

# Using activated venv
pytest
```

### Run Specific Test File
```bash
uv run pytest tests/test_login.py
```

### Run Specific Test
```bash
uv run pytest tests/test_login.py::TestLogin::test_successful_login_standard_user
```

### Run with Different Options
```bash
# Verbose output
uv run pytest -v

# Show print statements
uv run pytest -s

# Run only smoke tests
uv run pytest -m smoke

# Stop on first failure
uv run pytest -x

# Run in headless mode (no browser UI)
uv run pytest --headed false
```

1. **Run tests** (generates allure-results/):
```bash
uv run pytest
```

2. **Generate HTML report**:
```bash
allure generate allure-results -o allure-report --clean
```

3. **Open report in browser**:
```bash
allure open allure-report
```

## Docker 

Docker allows you to run tests in an isolated, consistent environment and view Allure reports from your host machine.

### Build Image
```bash
# Option 1: Using Make
make docker-build

# Option 2: Direct Docker command
docker build -t saucedemo-auth-automation:latest .
```

### Run Tests with Allure Report

#### Method 1: Using Make (Recommended)
```bash
make docker-test
```

#### Method 2: Using Docker Compose
```bash
make docker-test-compose
# or directly:
docker-compose up --build
```

#### Method 3: Direct Docker Run
```bash
docker run --rm -p 8080:8080 \
  -v $(PWD)/allure-results:/app/allure-results \
  -v $(PWD)/allure-report:/app/allure-report \
  saucedemo-auth-automation:latest
```

### What Happens in Docker

When you run tests in Docker:
1. **Tests execute** - All tests run in Chromium (headless)
2. **Results saved** - Test results saved to `allure-results/`
3. **Report generated** - Allure HTML report created in `allure-report/`
4. **Server starts** - HTTP server serves the report on port 8080

### View Report from Host Machine

#### Option 1: Access via Browser (While Container Runs)
Open your browser and navigate to:
```
http://localhost:8080
```

The Allure report will be accessible while the container is running!

#### Option 2: Open Report Locally (After Container Stops)
If the container has stopped, you can still view the report from the mounted volumes:

```bash
# Option A: Using Allure CLI
allure open allure-report

# Option B: Using Python HTTP server
cd allure-report && python3 -m http.server 8000
# Then open: http://localhost:8000
```

### Understanding Volume Mounts

The `-v` flags mount local directories into the container:
- `-v $(PWD)/allure-results:/app/allure-results` - Test results persist on host
- `-v $(PWD)/allure-report:/app/allure-report` - HTML report persists on host

This means even after the container stops, you'll have the reports on your local machine!
## Test Scenarios Covered

### 1. Successful Login (`test_successful_login_standard_user`)
- **User**: `standard_user` / `secret_sauce`
- **Expected**: Login succeeds, navigates to inventory page
- **Validates**: URL, inventory container visible, products displayed

### 2. Invalid Password (`test_login_with_invalid_password`)
- **User**: `standard_user` / `wrong_password`
- **Expected**: Login fails with error message
- **Validates**: Error message displayed, remains on login page

### 3. Locked User (`test_login_with_locked_out_user`)
- **User**: `locked_out_user` / `secret_sauce`
- **Expected**: Login fails with "locked out" error
- **Validates**: Specific error message for locked users

### 4. Empty Fields (`test_login_with_empty_fields`)
- **User**: (empty) / (empty)
- **Expected**: Validation error
- **Validates**: "Username is required" message appears

### 5. Performance User (`test_login_with_performance_glitch_user`)
- **User**: `performance_glitch_user` / `secret_sauce`
- **Expected**: Login succeeds despite delays
- **Validates**: Page loads correctly even with slow response

## License

This project is licensed under the MIT License.

## Author

Viktoria Kutseva
- GitHub: [@ViktoriaKutseva](https://github.com/ViktoriaKutseva)
