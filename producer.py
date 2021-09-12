import pika
import sys

if (len(sys.argv) != 5):
    print('You need to introduce server IP, Port, RabbitMQ user and password')

dir_ip = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]

connection = pika.BlockingConnection(pika.ConnectionParameters(dir_ip, port, '/', pika.PlainCredentials(user, password)))
channel = connection.channel()
print("Runnning Producer Application...")
print("Type in a task to be send")

while channel:
    task = input()
    channel.basic_publish(exchange='my_exchange', routing_key='test', body=task)

connection.close()