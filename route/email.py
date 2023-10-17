from fastapi import APIRouter,HTTPException,status,Body
from pydantic import EmailStr, BaseModel
from typing import List
import smtplib ,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

emailPath = APIRouter()
# class EmailBody(BaseModel):
#     to: str
#     subject: str
#     message: str
@emailPath.post("/email/1")
async def send_email():
    return "tst"

@emailPath.post("/email")
async def send_email():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "skyrock999@gmail.com"  # Enter your address
    receiver_email = "earthyado999@gmail.com"  # Enter receiver address
    password = "xnbkrrgvbcvqdsnr"
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""
    html = """\
    <html>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <a href="http://www.realpython.com">Real Python</a> 
        has many great tutorials.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    # message = """\
    # Subject: Hi there

    # This message is sent from Python."""
    # contexts = ssl.create_default_context()
    
    # with smtplib.SMTP_SSL(smtp_server,port,context=contexts) as smtp:
    #     smtp.login(sender_email, password)
    #     smtp.sendmail(sender_email, receiver_email, message)
    return {"message": "Email sent successfully"}
    # try:
    #     with smtplib.SMTP_SSL('smtp.gmail.com',3000) as smtp:
    #         smtp.login(email,pass_e)
    #         smtp.send_message(msg)
    #     return {"message": "Email sent successfully"}
    # except:
    # # handle the exception
    #     return {"message": "fail"}
    
        
  

