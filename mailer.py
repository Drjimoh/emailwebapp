import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, send_to, subject, text, files=[], server="localhost"):
    assert type(send_to)==str
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP('mail.xxxx.com:587')
    smtp.ehlo()
    smtp.starttls()
    smtp.login('xxxx@xxx.com','xxpasswordxxx')
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

ATTACHMENTS = ['/path_to_attachment_file']
send_from='xxxx@xxxx.com'
send_to='xxxx@xxxx.com'
subject='Testing my Email Prowress'
text = 'Yo yo are you with you'
send_mail(send_from, send_to, subject, text, files=ATTACHMENTS)
