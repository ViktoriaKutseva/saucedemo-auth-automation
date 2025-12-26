FROM python:3.10-slim

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

RUN apt-get update && apt-get install -y \
    ca-certificates \
    openjdk-21-jre-headless \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml ./
COPY src/ ./src/
COPY tests/ ./tests/ 

RUN uv sync

RUN uv run playwright install chromium --with-deps

# Install Allure CLI
RUN apt-get update && apt-get install -y wget unzip openjdk-21-jre-headless && \
    wget -O allure.zip https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.zip && \
    unzip allure.zip -d /opt/ && \
    ln -s /opt/allure-2.25.0/bin/allure /usr/local/bin/allure && \
    rm allure.zip && \
    apt-get remove -y wget unzip && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

RUN mkdir -p allure-results allure-report

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Expose port for Allure report server
EXPOSE 8080

CMD ["sh", "-c", "uv run pytest tests/ --alluredir=/app/allure-results && allure generate /app/allure-results -o /app/allure-report --clean && cd /app/allure-report && python3 -m http.server 8080"]
