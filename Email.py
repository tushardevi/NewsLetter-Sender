import smtplib
from API_Data import*

def SendEmail(email,name):
    # add text
    greet = "Hi" + " " + name + "."
    sentence = "Today's latest news:"

    message ="""<html>
        <body>
            <head>
            <style="color:red">
            <font size="5"><div class='container'>{gr}
            <font size="4"><div class='container'>{sen}</body>
            </head>
      </html>""".format(gr=greet, sen = sentence)


    # setup the parameters of the message
    password = 'jettbxrudxdhcsof'
    msg['From'] = 'pythoncplusplus69@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'BBC'


    # add in the message header and body
    header = MIMEText(message, 'html')
    content = MIMEText(html, 'html')



    msg.attach(MIMEText(button,'html'))
    msg.attach(header)
    msg.attach(content)


    # create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    emails = ["pythoncplusplus69@gmail.com"]

    # send the message via the server.
    #for email in obj:
    server.sendmail(msg['From'], email, msg.as_string())
    print("email sent successfully to %s:" % email)

    server.quit()


