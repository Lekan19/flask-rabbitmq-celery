from celery import Celery

celery_app = Celery('tasks', broker='amqp://user:nopassword@rabbitmq:5672/addition', backend='rpc://')

@celery_app.task
def add(x, y):
    return x + y