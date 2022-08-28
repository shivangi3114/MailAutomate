#import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

#from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp_mailoutlook.com"

# Load the environment variables
#current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
#envars = current_dir / ".env"
#load_dotenv(envars)

# Read environment variables
sender_email =  "shivangi.khare1@outlook.com"
password_email =   "Chinki@31"

def send_email(subject, receiver_email, name, date):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Remainder MOM", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        I hope you are well.
        I just wanted to drop you a quick note to remind you that on {date} i.e today you should take Minutes for teams meet.
        I would be really grateful if you could confirm that everything is on track for todays meet.
        
        Best regards
        Mohammed
        """
    )
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
   	f"""
    	<html>
      <body>
        <p>Hi {name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that on <strong>{date}</strong> we have a meeting .</p>
        <p>I would be really grateful if you could confirm that everything is on track for the meeting.</p>
        <p>Best regards</p>
        <p>YOUR NAME</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject=" Reminder",
        name="Mohammed",
        receiver_email="emailasfan@gmail.com",
        date="25, Aug 2022",
        
    )
