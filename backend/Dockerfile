FROM python:3.11-slim

WORKDIR /app

# Install uv for fast dependency resolution and installation
RUN pip install uv

# Copy the pyproject.toml
COPY pyproject.toml .

# Install dependencies directly to system (safe since this is a container)
RUN uv pip install --system fastapi uvicorn python-socketio motor pydantic

# Copy application files
COPY ./app ./app

# Expose backend port
EXPOSE 8000

# Start Application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
