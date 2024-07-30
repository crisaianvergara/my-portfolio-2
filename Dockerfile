FROM python:3.12.1
WORKDIR /my_portfolio

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt /my_portfolio/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . /my_portfolio/

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_portfolio.wsgi:application"]