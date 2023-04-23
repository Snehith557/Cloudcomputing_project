import pika


# updating the user data
# Set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',port=5672))
channel = connection.channel()
#channel.queue_declare(queue='add_queue')
channel.queue_declare(queue='update_queue')

# Send a message to RabbitMQ to insert data
#message = "John,30"
#adding the data
srn=input("Enter the srn :")
srn = srn+','
age = input("Enter the updated age :")
message = srn+age
channel.basic_publish(exchange='', routing_key='update_queue', body=message)


# Close the connection
connection.close()

