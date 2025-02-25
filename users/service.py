from django.core.mail import send_mail

def send_email():
    send_mail(
        subject='Test Message',
        # message='test message',
        from_email='samariddin.grex@gmail.com',
        recipient_list=['samariddin.grex@gmail.com'],
        html_message="""
            <main>
                <h1>Hush kelibsiz</h1>
            </main>
        """
    )
