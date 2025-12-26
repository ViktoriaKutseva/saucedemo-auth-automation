FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libwayland-client0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    openjdk-21-jre-headless \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install chromium --with-deps

# Install Allure CLI
RUN apt-get update && apt-get install -y wget unzip && \
    wget -O allure.zip https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.zip && \
    unzip allure.zip -d /opt/ && \
    ln -s /opt/allure-2.25.0/bin/allure /usr/local/bin/allure && \
    rm allure.zip && \
    apt-get remove -y wget unzip && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

COPY src/ ./src/
COPY tests/ ./tests/ 

RUN mkdir -p allure-results

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

CMD ["pytest", "tests/", "--browser", "chromium"]