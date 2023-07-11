# Base image
FROM python:3.9

# Set working directory
WORKDIR /todo

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to working directory
COPY . /todo/

# Run migrations and collect static files
RUN python manage.py migrate && \
    python manage.py collectstatic --no-input

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Expose port
EXPOSE ${PORT}

# Start server
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:${PORT}", "--workers", "2"]
