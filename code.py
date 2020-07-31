
#   Code to check the validity of an email address
# it is not completed. it splits the email address into 2 parts. the part after "@" is always a website.
# therefore, this code checks if the website really exists or not. if it exists, it means the email is valid.

# the reason that is code is not complete is because not every valid website is a mailing site
# or example, i think there is no email address that goes like this: someone@youtube.com
# although, youtube.com is a valid website. But this email is not valid.

import requests as req
# from bs4 import BeautifulSoup as soup
try:
    in_email = input("Enter the email address to check its validity: ")

    if in_email.find('@') < 0:
        print("The entered email is not in the correct form")

    else:
        # separating the part of email after the "@"
        split_email = in_email.split('@')
        to_check = split_email[1]
        e_site = "http://" + to_check
        print(e_site)
        e_check = req.get(e_site)

        if e_check:
            print("The website is valid")

except:
    print("Sorry, the email is invalid")