import pika, sys

if (len(sys.args) != 5):
    print('You need to introduce server IP, Port, RabbitMQ user and password')

dir_ip = sys.args[1]
port = sys.args[2]
user = sys.args[3]
password = sys.args[4]

connection = pika.BlockingConnection(pika.ConnectionParameters(dir_ip, port, '/', pika.PlainCredentials(user, password)))
channel = connection.channel()
print("Runnning Producer Application...")
print("Type in a task to be send")

while channel:
    task = input()
    channel.basic_publish(exchange='my_exchange', routing_key='test', body=task)

connection.close()