# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

RUN python manage.py createsuperuser

# Define environment variable
RUN python manage.py makemigrations && python manage.py migrate

# Run app.py when the container launches
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 & python manage.py runbot"]