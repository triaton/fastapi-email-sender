from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendMailDto(BaseModel):
    recipient: str
    content: str
    subject: str

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, world!'}

@app.post('/send-mail')
async def send_email(payload: SendMailDto):
    load_dotenv(verbose=True)
    smtp_host = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    s = smtplib.SMTP(host=smtp_host, port=smtp_port)
    s.starttls()
    s.login(sender_email, sender_password)
    msg = MIMEMultipart()

    msg['From'] = sender_email
    msg['To'] = payload.recipient
    msg['Subject'] = payload.subject
    msg.attach(MIMEText(payload.content, 'plain'))
    s.send_message(msg)

    return {'recipient': payload.recipient, 'content': payload.content}
