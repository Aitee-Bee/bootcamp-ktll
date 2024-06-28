"""
Create a tuple of 6 email adresses, then write a function
that takes the tuple as argument. The function will check if the
email is not ending with a ".com", it will change it to a ".com"
and add it to a list. If it is ending with a ".com", it will
simply just add it to the list. Then will return the list.

'wilson@gmail.net', 'swedishgee@yahoo.com', 'pelstop@gmail.com', 'deniah@gmail.edu'
"""

email_address = ("'wilson@gmail.net', 'swedishgee@yahoo.com', 'pelstop@gmail.com', 'deniah@gmail.edu'")


def check_email(email_address):
    clean_emails = []
    for email in email_address:
        dot = email.index(".")
        root = email[dot:]
        if root != ".com":
            new_email = email[:dot] + ".com"
            clean_emails.append(new_email)
        else:
            clean_emails.append(email)
    return clean_emails


print(check_email('wilson@gmail.net'))







