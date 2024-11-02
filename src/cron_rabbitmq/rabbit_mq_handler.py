import pika
from src.subscribe.service import SubscribeService
from src.db.dependencies import get_db


service = SubscribeService()

async def send_user_info_to_rabbitmq(sender_id, username, first_name, last_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='user_auth')

    message = f"sender_id={sender_id}, username={username}, first_name={first_name}, last_name={last_name}"
    channel.basic_publish(exchange='', routing_key='user_info_queue', body=message)
    connection.close()


def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='your_rabbitmq_host'))
    channel = connection.channel()
    channel.queue_declare(queue='user_auth')

    def callback(ch, method, properties, body):
        sender_id, username, first_name, last_name = body.decode().split(',')
        # Add user information to the database
        service.store_tg_user_info(sender_id, username, first_name, last_name, get_db)
        

    channel.basic_consume(queue='user_info_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()