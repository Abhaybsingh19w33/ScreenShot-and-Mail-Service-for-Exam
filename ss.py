import os
import os.path

import mss

from datetime import datetime

now = datetime.now()
now = str(now)
now = now.split(" ")
data1 = now[0]
data2 = now[1]
data1 = data1.split("-")
data2 = data2.split(".")
data2 = data2[0].split(":")

now = ""
for i in data1:
    now = now + i
for i in data2:
    now = now + i

with mss.mss() as sct:
    filename = sct.shot(output=now + ".png")
    # print(filename)

# --------------------------------------------------

# ssary libraries
import img2pdf
from PIL import Image
import os

# storing image path
img_path = os.getcwd()
# print(img_path)
img_path = img_path + "\\" + now + ".png"

# storing pdf path
pdf_path = os.getcwd() + "\\" + now + ".pdf"
open(now + ".pdf", "w")

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")

# ---------------------------------------------------

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail_content = ""
# The mail addresses and password

sender_address = ""
sender_pass = ""
receiver_address = ""
# Setup the MIME
message = MIMEMultipart()
message["From"] = sender_address
message["To"] = receiver_address
message["Subject"] = "A test mail sent by Python. It has an attachment."
# The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, "plain"))
attach_file_name = pdf_path
# attach_file_name = now + ".pdf"
attach_file = open(attach_file_name, "rb")  # Open the file as binary mode
payload = MIMEBase("application", "octate-stream")
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)  # encode the attachment
# add payload header with filename
payload.add_header("Content-Decomposition", "attachment", filename=attach_file_name)
message.attach(payload)
# Create SMTP session for sending the mail
session = smtplib.SMTP("smtp.gmail.com", 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print("Mail Sent")
