import pika
import time
import random

connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue="letter_box")

message_count = 0

while True:

    message = f'Message {message_count}'

    channel.basic_publish(exchange="", routing_key="letter_box", body=message)

    print(f" [x] Sent '{message}'")

    time.sleep(random.randint(1, 4))


    message_count += 1

    