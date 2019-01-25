#!/usr/bin/env python3                                                         
import os
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

form = cgi.FieldStorage()
f_username = form.getfirst("username")
f_password  = form.getfirst("password")

request_type = os.environ.get("REQUEST_METHOD", "GET")
cookie_string = os.environ.get("HTTP_COOKIE")

cookie_kvs = cookie_string .split("; ")

c_username = None
c_password = None
'''
for cookie_kv in cookie_kvs:
    k, v = cookie_kv .split('=')
    if cookie_kv:
        if k == "username":
            c_username = v
        if cookie_kv:
            if k == "password":
                c_password = v
'''               
try:
    cookie_string = os.environ.get("HTTP_COOKIE")
    cookie_pairs = cookie_string.split(";") # gives me ["key=val"] 
    for pair in cookie_pairs:
        key, val = pair.split("=")
        if "username" in key:
            c_username = val
        elif "password" in key:
            c_password = val
except:
    pass
        
        
print("Content-Type: text/html")

if c_username and c_password:
    print()
    print(secret_page(c_password, c_password))

        
        
if request_type == "POST":
    if f_username == username and f_password == password:
        #Login ok, set cookie
        print("Set-Cookie: username={}".format(f_username))
        print("Set-Cookie: password={}".format(f_password))
        print("\n\n")
        print(secret_page(f_username,f_password))
    else:
        print("\n\n")
        print(after_login_incorrect())
else:
    print("\n\n")
    print(login_page())
    print(cookie_string)
    



