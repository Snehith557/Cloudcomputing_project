# Use the official Python image as the base image
FROM python:3

# Set the working directory to /app
WORKDIR /del_p

# Copy the current directory contents into the container at /app
COPY . /del_p

# Install the required Python packages
RUN pip install pika
RUN pip install pymysql

# Set the command to run the Python script
CMD ["python3", "delete.py"]

