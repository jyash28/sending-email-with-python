import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr="jyash548@gmail.com"
to_aadr=["vinaygupta7516@gmail.com","yash.04may@gamil.com"]
msg=MIMEMultipart()
msg["From"]=from_addr
msg["To"]=" ,".join(to_aadr)
msg["Subject"]="just to check"

body="hello world"
msg.attach(MIMEText(body,"plain"))

email="your email address"
password="your password"


conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login(email,password)
text=msg.as_string()

conn.sendmail(from_addr,to_aadr,text)
conn.quit()