from flask.ext.mail import Message
from __init__ import app, mail
from config import ADMINS
msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)
