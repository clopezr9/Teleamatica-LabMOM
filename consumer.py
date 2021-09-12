import pika
import sys

if (len(sys.argv) != 5):
    print('You need to introduce server IP, Port, RabbitMQ user and password')
else:
    dir_ip = sys.argv[1]
    port = sys.argv[2]
    user = sys.argv[3]
    password = sys.argv[4]

connection = pika.BlockingConnection(pika.ConnectionParameters(dir_ip, port, '/', pika.PlainCredentials(user, password)))
channel = connection.channel()

def callback(ch, method, properties, body):
    print('Task:' + body + 'is received')

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()