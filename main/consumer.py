import pika

params = pika.URLParameters('amqps://wbwqtgwy:E-OlzLdn3tnj1YgzH2xlV7kDhRAI4bQQ@shrimp.rmq.cloudamqp.com/wbwqtgwy')

connection = pika.BlockingConnection(params)

channel = connection.channel()  # start a channel

channel.queue_declare(queue='main')  # Declare a queue

def callback(ch, method, properties, body):
    print("Received in main")
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('MAIN: Started Consuming')

channel.start_consuming()

channel.close()