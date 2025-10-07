import pika

def on_message(ch, method, properties, body):
    print(f" [x] Received '{body}'")
connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='letter_box'
                      )

channel.basic_consume(queue='letter_box',
                      auto_ack=True,on_message_callback=on_message)

print('starting consuming')