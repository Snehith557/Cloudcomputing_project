# consumer file for adding and deleting the data
import pika
import pymysql

# Set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='add_queue')
channel.queue_declare(queue='delete_queue')
channel.queue_declare(queue='update_queue')
channel.queue_declare(queue='health_check')

# Set up MySQL connection
#mysql_connection = mysql.connector.connect(
 #   host="localhost",
  #  user="yourusername",
   # password="yourpassword",
#    database="mydatabase"
#)
#mysql_cursor = mysql_connection.cursor()


# Set up MySQL connection

connection = pymysql.connect(
    host='localhost',
    user='snehith',
    password='snehith',
    db='microservice',
    cursorclass=pymysql.cursors.DictCursor
)

# Define callback functions
def insert_callback(ch, method, properties, body):
    # Parse message body
    
    with connection.cursor() as cursor:
    	srn, age = body.decode().split(",")

    # Insert data into MySQL
    	sql = "INSERT INTO data (srn, age) VALUES (%s, %s)"
    	val = (srn, age)
    	cursor.execute(sql, val)
    	connection.commit()
    	#connection.close()

    	print("Inserted data:", srn, age)

def delete_callback(ch, method, properties, body):
    # Parse message body
	with connection.cursor() as cursor:
		srn = body.decode()
	
    # Delete data from MySQL
		sql = "DELETE FROM data WHERE srn = %s"
		val = (srn)
		cursor.execute(sql, val)
		connection.commit()
		connection.close()
#print("Deleted data for:",name)



def update_callback(ch, method, properties, body):
    # Parse message body
	with connection.cursor() as cursor:
		srn,age = body.decode().split(",")
		
    # updating data in MySQL based on the name/SRN
    # a sql query to modify the age based on srn
		#sql = "DELETE FROM data WHERE name = %s"
		sql = "UPDATE data SET age = %s WHERE srn = %s"

		val = (age,srn)
		cursor.execute(sql,val)
		connection.commit()
		connection.close()
#    		print("Deleted data for:",name)



# Define the callback function
def health_callback(ch, method, properties, body):
    #queue_name = input("Enter the queue name :")
    queue = channel.queue_declare(queue=body.decode(), passive=True)
    # check the health of this queue
#@#    kn,
    #queue_name = body.decode()
    #print(queue_name) 
    queue_size = queue.method.message_count
    if channel.is_open:
        print("RabbitMQ is healthy")
        print("Number of messages in the %s queue: %d" % (queue, queue_size))
    else:
        print("RabbitMQ is not healthy")










# Start consuming messages from RabbitMQ


#channel.basic_consume(queue='health_check', on_message_callback=health_callback, auto_ack=True)
channel.basic_consume(queue='add_queue', on_message_callback=insert_callback, auto_ack=True)
channel.basic_consume(queue='delete_queue', on_message_callback=delete_callback, auto_ack=True)
channel.basic_consume(queue='update_queue', on_message_callback=update_callback, auto_ack=True)
channel.basic_consume(queue='health_check', on_message_callback=health_callback, auto_ack=True)

channel.start_consuming()
