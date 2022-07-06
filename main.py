import urllib.request
import random

url = input("enter url to scrape\n")
name=input("enter name of file\n")
response = urllib.request.urlopen(url)

charsets = response.info().get_charsets()
if len(charsets) == 0 or charsets[0] is None:
    charset = 'utf-8'
else:
    charset = charsets[0]

userIp = response.read().decode(charset).strip()

f=open(name+".html","w")
print(userIp)
