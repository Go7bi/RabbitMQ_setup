import pika
import random
import time

def on_message(ch, method, properties, body):

    processing_time = random.randint(1, 6)
    print(f" [x] Received '{body}' on processing time {processing_time} seconds")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(' [x] Done')

connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue='letter_box'
                      )

#channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letter_box',
                      on_message_callback=on_message)

print('starting consuming')

channel.start_consuming()