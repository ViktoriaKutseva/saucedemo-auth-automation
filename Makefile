.PHONY: help install test test-headed report clean docker-build docker-test lint format


help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'


install:  ## Install dependencies
	uv sync
	uv run playwright install chromium

test:  ## Run tests in headless mode
	uv run pytest --headed false

test-headed:  ## Run tests with visible browser
	uv run pytest --headed

test-smoke:  ## Run only smoke tests
	uv run pytest -m smoke

report:  ## Generate and open Allure report
	allure generate allure-results -o allure-report --clean
	allure open allure-report

clean:  ## Clean generated files
	rm -rf allure-results allure-report .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docker-build:  ## Build Docker image
	docker build -t saucedemo-auth-automation:latest .

docker-test:  ## Run tests in Docker with Allure report
	docker run --rm -p 8080:8080 \
		-v $(PWD)/allure-results:/app/allure-results \
		-v $(PWD)/allure-report:/app/allure-report \
		saucedemo-auth-automation:latest

lint:  ## Run code quality checks
	uv run ruff check src tests

format:  ## Format code
	uv run ruff format src tests