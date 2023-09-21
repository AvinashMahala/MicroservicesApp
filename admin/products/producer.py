import pika, json

params = pika.URLParameters('amqps://wbwqtgwy:E-OlzLdn3tnj1YgzH2xlV7kDhRAI4bQQ@shrimp.rmq.cloudamqp.com/wbwqtgwy')

connection = pika.BlockingConnection(params)

channel = connection.channel()  # start a channel


# def publish():
#     channel.basic_publish(exchange='', routing_key='main', body='Hello Main!')


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
