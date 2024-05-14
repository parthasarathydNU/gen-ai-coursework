# Use an official Python runtime as parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application code
COPY . .

# Command to run on container start
CMD ["python", "scripts/starter_test.py"]
