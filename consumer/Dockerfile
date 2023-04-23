# Use a Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /consumer

# Copy the current directory contents into the container at /app
COPY . /consumer

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install pika
RUN pip install pymysql
# Make port 5672 available to the world outside this container


# Run app.py when the container launches
CMD ["python3", "consumer.py"]

