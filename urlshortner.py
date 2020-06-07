import requests 
import pyshorteners
url =input('enter the API HERE ---->>>')
# response=requests.get(url)
# print(response.text)



s=pyshorteners.Shortener()


print('the shortned url is this -->> ',s.tinyurl.short(url))