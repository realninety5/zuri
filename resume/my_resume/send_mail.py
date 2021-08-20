
from email.mime import multipart
import smtplib, os
from email.message import EmailMessage

# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================
gmail_user = os.getenv('my_mail')
gmail_app_password = os.getenv('mail_pass')


def mail(subject, body, from_mail):
 
    msg = EmailMessage()
    msg['from'] = from_mail
    msg['to'] =[gmail_user]
    msg['subject'] = subject
    msg.set_content(body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, os.getenv('mail_pass'))
        server.sendmail(from_mail, gmail_user, msg.as_string())
        server.close()


        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
