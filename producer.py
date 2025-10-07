import pika

connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue="letter_box")

message = "Hi balajiiii"

channel.basic_publish(exchange="", routing_key="letter_box", body=message)

print(f" [x] Sent '{message}'")

connection.close()