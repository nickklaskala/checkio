#!/usr/bin/env checkio --domain=py run sendgrid-sendone

# To solve this mission you must use theSendGrid API Key(this video will explainhow to create your own API Key). Check out thesePython examples.
# 
# It all starts with your first email. Let’s try to send one.
# 
# Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and the name of the user.
# 
# Subject of the email should be "Welcome" and body simply "Hi {name}" ({name} should be replaced by a user's name)
# 
# Input:Two arguments: email and a username.
# 
# Output:None. You should send an email. You don’t need to return anything.
# 
# 
# send_email('a.lyabah@checkio.org', 'oduvan')
# send_email('somebody@gmail.com', 'Some Body')
# 
# END_DESC

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