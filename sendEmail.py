import os, ssl, smtplib


def sendEmail(receiver=os.getenv('PYEMAIL'), message='Subject: Test'):
    host = 'smtp.gmail.com'
    port = 465

    userName = os.getenv('PYEMAIL')
    password = os.getenv('PYPW')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as email:
        email.login(userName, password)
        email.sendmail(userName, receiver, message)


if __name__ == '__main__':
    receiver = os.getenv('PYEMAIL')
    message = """Subject: Hi!

        How are you?
        Bye!
        """
    sendEmail()
