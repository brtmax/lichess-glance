FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libcairo2 \
    libcairo2-dev \
    libffi-dev \
    libpango-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY lichess_puzzle_server.py .

EXPOSE 5000

CMD ["python", "lichess_puzzle_server.py"]
