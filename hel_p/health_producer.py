import pika

# Set the connection parameters
#connection_params = pika.ConnectionParameters('127.0.0.1',port=5672)
#credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1',port=5672))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='health_check')

# Send a message to the queue



print("Exisiting Queues : add_queue ,delete_queue,update_queue,health_check")
message = input("Enter the name of the queue :")
#print(queue)
channel.basic_publish(exchange='',routing_key='health_check',body=message)

# Close the connection
connection.close()

