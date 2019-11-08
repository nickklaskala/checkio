#!/usr/bin/env checkio --domain=py run sendgrid-sendone




import sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
SUBJECT = 'Welcome'
BODY = 'Hi {}'
FROM_EMAIL = 'nick.klaskala@outlook.com'

sg = sendgrid.SendGridAPIClient(API_KEY)

def send_email(email, name):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=BODY.format(name)
    )
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('nklaskala@yahoo.com', 'Nick Klaskala')
