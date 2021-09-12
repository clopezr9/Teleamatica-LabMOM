import pika
import sys

if (len(sys.argv) != 5):
    print('You need to introduce server IP, Port, RabbitMQ user and password')
else:
    dir_ip = sys.argv[1]
    port = sys.argv[2]
    user = sys.argv[3]
    password = sys.argv[4]

task = ''

connection = pika.BlockingConnection(pika.ConnectionParameters(dir_ip, port, '/', pika.PlainCredentials(user, password)))
channel = connection.channel()
print("Runnning Producer Application...")
print("Type in a task to be send")

while True:
    task = sys.stdin.readline()
    if (len(task) != 0):
        channel.basic_publish(exchange='my_exchange', routing_key='test', body=task)
        print( task + 'send succesfully!')
