import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.exchange_declare(exchange='topic', exchange_type=ExchangeType.topic)

user_payment_message = "this is user payment message"
channel.basic_publish(exchange="topic", routing_key="user.erope.payment", body=user_payment_message)

print(f" [x] Sent '{user_payment_message}'")

bussines_paymet_message = "this is eropoen payment message"
channel.basic_publish(exchange="topic", routing_key="business.europe.order", body=bussines_paymet_message)

print(f" [x] Sent '{bussines_paymet_message}'")

connection.close()