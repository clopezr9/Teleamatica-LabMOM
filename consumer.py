import pika, sys

if (len(sys.args) != 2):
    print('You need to introduce server IP, Port, RabbitMQ user and password')

dir_ip = sys.args[1]
port = sys.args[2]
user = sys.args[3]
password = sys.args[4]

connection = pika.BlockingConnection(pika.ConnectionParameters(dir_ip, port, '/', pika.PlainCredentials(user, password)))
channel = connection.channel()

def callback(ch, method, properties, body):
    print('Task:' + body + 'is received')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()