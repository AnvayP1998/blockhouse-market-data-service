# Step 1: Base image
FROM python:3.10-slim

# Step 2: Set workdir
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy app code
COPY app ./app

# Step 5: Expose port (for Uvicorn)
EXPOSE 8000

# Step 6: Run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
