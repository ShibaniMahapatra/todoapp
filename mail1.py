import smtplib

from_addr ="shibani.new97@gmail.com"
to_addr_list = ['s19.mahapatra@gmail.com']
cc_addr_list = ['']
subject= 'Howdy'
message = 'Howdy from a python function'
login= 'Shibani'
password = ''
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s' % from_addr
    header += 'To: %s' % ', '.join(to_addr_list)
    # header += 'Cc: %s' % ', '.join(cc_addr_list)
    header += 'Subject: %s' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587')