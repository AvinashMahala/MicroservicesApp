import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://wbwqtgwy:E-OlzLdn3tnj1YgzH2xlV7kDhRAI4bQQ@shrimp.rmq.cloudamqp.com/wbwqtgwy')

connection = pika.BlockingConnection(params)

channel = connection.channel()  # start a channel

channel.queue_declare(queue='admin')  # Declare a queue

def callback(ch, method, properties, body):
    print("ADMIN : Received in admin")
    data=json.loads(body)
    print(data)
    product=Product.objects.get(id=data)
    product.likes=product.likes+1
    product.save()
    print('Product Likes Increased!')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()