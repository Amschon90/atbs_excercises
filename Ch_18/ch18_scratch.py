import smtplib
import gmail_credentials

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# if 250 returns, that means success
smtpObj.ehlo()

# if 220 returns, that means ready
smtpObj.starttls()

smtpObj.login(gmail_credentials.username,gmail_credentials.password)

smtpObj.sendmail(f'{gmail_credentials.username}', 'kronozftw@gmail.com', 'Subject: Hello!\nHello World.')