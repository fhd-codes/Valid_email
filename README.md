# Valid_email
This is a python code that checks the validity of an email address


There are so many websites that it is practically impossible to make a database and scan it to match the entered email address with it for its validity. Every company has their custom email addresses. 
It is to be noted that email address has the following main components

    "text" + "@" + "text" + "." + "text"
for example, someone@gmail.com
or someone@company.com.pk (etc.)

It is to be noted that after the "@" sign, whatever written is always a website (correct me if I am wrong)
So, what this code does if that it splits the entered email address into 2 parts (1) before @-sign and (2) after the @-sign
Then by using "requests" library, it checks if the second part (of the email after splitting) is a valid website or not??
If the website gives response, it means that the entered email most probably has a valid domain.

# NOTE:

This code is not completed.

The reason that this code is not complete is because not every valid website is a mailing site
For example, i think there is no email address that goes like this: someone@youtube.com
Although, youtube.com is a valid website. But this email is not valid.
