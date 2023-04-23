# Use the official Python image as the base image
FROM python:3

# Set the working directory to /app
WORKDIR /update_p

# Copy the current directory contents into the container at /app
COPY . /update_p

# Install the required Python packages
RUN pip install pika
RUN pip install pymysql

# Set the command to run the Python script
CMD ["python3", "update.py"]

