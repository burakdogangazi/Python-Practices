# mail üzerinden google da daha az güvenli uygulamalara izin veri açık yapmalıyız

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()

mesaj["From"] = "ddoganbburak@gmail.com"

mesaj["To"] = "ddoganbburak@gmail.com"

mesaj["Subject"] = "Smtp Mail Gönderme"

yazi = """

    Smtp ile mail gönderiyorum

    Burak Doğan

"""

mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)


try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo() # bagladık kendimizi smtp serverına

    mail.starttls() # şifremizi cryptler

    mail.login("ddoganbburak@gmail.com","Burak1q2w@!")

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    print("Mail başarıyla gönderildi")

    mail.close()#smtp serverdan bağlantı kestik kesinlikle yapılmalı


except:
    sys.stderr.write("Bir Sorun Oluştu..")
    sys.stderr.flush()















