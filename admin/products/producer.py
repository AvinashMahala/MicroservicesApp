import pika

params = pika.URLParameters('amqps://wbwqtgwy:E-OlzLdn3tnj1YgzH2xlV7kDhRAI4bQQ@shrimp.rmq.cloudamqp.com/wbwqtgwy')

connection = pika.BlockingConnection(params)

channel = connection.channel()  # start a channel

# channel.queue_declare(queue='producer')  # Declare a queue

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello Avinash!')

