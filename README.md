# Teleamatica-LabMOM
## Autor: Catalina López Roldán
## Descripción
En este laboratorio se puede evidenciar el uso de un middleware para el envio de tareas indepenidentes a diferentes consumidores. Para esto usaremos un MOM llamado RabittMQ usando el protocolo de MAQP 0-9-1.

## Prerrequisitos
- RabbitMQ instalado y configurado.
- Python 3.0 o superior.

## Instalación
Debe contar con python 3, ademas de git y un edito de texto de preferencia, se pueden instalar con los siguientes comandos:
<pre><code> $ sudo yum install git
 $ sudo yum install emacs 
 $ sudo yum install python3
</code></pre>

Ademas se debe installar la biblioteca de pika con el siguiente comando:
<pre><code> $ python3 -m pip install pika
</code></pre>

## Ejecución
Para ejecutar el programa clonar este repositorio y los prerequisitos necesarios.
Luego de verificar esto se puede correr el consumer.py de la siguiente manera:
<pre><code> $ python3 consumer.py [DIR_IP] [PUERTO] [RabbitMQ_User] [RabbitMQ_Password]
</code></pre>

Luego se puede correr el producer.py de la siguiente manera:
<pre><code> $ python3 producer.py [DIR_IP] [PUERTO] [RabbitMQ_User] [RabbitMQ_Password]
</code></pre>
DIR_IP: La IP publica de la instancia en la que esta configurado el RabittMQ. <br />
PUERTO: El puerto previamente seleccionado y abierto para TCP, generalmente 5672. <br />
RabbitMQ_User: Usuario usado en la configuración del RabbitMQ. <br />
RabbitMQ_Password: Contraseña usada en la configuración del RabbitMQ. <br />

## Referencias
- https://www.rabbitmq.com/consumer-prefetch.html
