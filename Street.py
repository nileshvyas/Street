# Define a function that will post on server every 15 Seconds 

import requests
import urllib.request 

def read_data_thingspeak():
  print("hello")
  b=5
  URl='https://api.thingspeak.com/update?api_key='
  KEY='B9RDBVP7MF9JYNEV'
  HEADER='&field1={}&field2={}'.format(b,b)
  NEW_URL=URl+KEY+HEADER
  print(NEW_URL)
  data=urllib.request.urlopen(NEW_URL)
  print(data)
 

if __name__ == '__main__':
  
  while(1):
    read_data_thingspeak()
    #thingspeak_post()
