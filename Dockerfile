FROM python:3.9-slim

# Install postgres dependencies and clean up apt in one layer
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Documentation: Tell Docker the app runs on 5000
EXPOSE 5000

CMD ["python", "app.py"]
