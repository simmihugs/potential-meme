# Use a lightweight Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies (only once during image build)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Command to run your FastAPI app (this will be overridden by docker-compose for development)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
