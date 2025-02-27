from django.core.mail import send_mail
from .utils import generate_code

def send_custom_code_email(user, to):
    send_mail(
        reset_link = '{% url "users:restore_password" %}',
        subject='Test Message',
        message="This is a fallback text message for email clients that don't support HTML.", 
        from_email='samariddin.grex@gmail.com',
        recipient_list=[to],
        name = user.username,
        code = generate_code,
        html_message="""
            <main>
                <h1> {name} okajon nedrozumeniya parolizni yangimoqchikansiz bratim!</h1>
                <b>{code}<b>
                <i>Shu linkga kirib 4 xonali kodni kiriting:</i>
                <a href="{reset_link}" class='btn btn-primary'>Parolni Tiklash</a>
                <p>Agar yangilamoqchi bo'lmasangiz hech nma qmen bratan!</p>
            </main>
        """,
    )

from threading import Thread

def send_thread_email(user, to):
    thread1 = Thread(target=send_custom_code_email, args=(user, to))
    thread1.start()