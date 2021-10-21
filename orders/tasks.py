from celery import shared_task
from django.conf import settings

from django.core.mail import message, send_mail

from .models import Order

@shared_task
def order_created(order_id):
    """Task to send an e-mail notification when an order is
       successfully created."""
    
    order = Order.objects.get(pk=order_id)
    subject = f'Order no {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
              f'You have successfully placed an order' \
              f'Your Order Id is {order.id}'
    mail_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])
    return mail_sent