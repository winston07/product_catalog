from django.core.mail import send_mail


def send_email(message, email_from, email_to):
    send_mail(
        'Subject: %s' % message[0],
        '%s' % message[1],
        email_from,
        email_to,
        fail_silently=False,
    )
