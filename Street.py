import urllib.request
import requests
import threading
import json
import time

import random


import datetime  
from datetime import timedelta

utc=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
print(utc)



#import datetime 
basedate=str(utc)
formatfrom="%Y-%m-%dT%H:%M:%S"
formatto="%H:%M:%S"
from datetime import datetime
current_time=datetime.strptime(basedate,formatfrom).strftime(formatto)




# Define a function that will post on server every 15 Seconds  
  
def read_data_thingspeak():
  threading.Timer(120,read_data_thingspeak).start()
  URL=' https://api.thingspeak.com/channels/538984/feeds.json?api_key='
  KEY='X34X42TNNLBL2J21'
  HEADER='&results=7'
  NEW_URL=URL+KEY+HEADER
  print(NEW_URL)

  get_data=requests.get(NEW_URL).json()
  print(get_data)
  channel_id=get_data['channel']['id']

  feild_1=get_data['feeds']
  print("field_1 :")
  print(feild_1)
 

  t=[]
  entry_id=[]
  time=[]
  for x in feild_1:
    #print(x['field1'])
    t.append(x['field1'])
    a=x['field1']
    print('a=',a)
    entry_id.append(x['entry_id'])
    time.append(x['created_at'])

  print("Entry Id: ")
  print(entry_id[6])
  print(time[6])
  basedate=time[6]
  print("BASE_TIME: ",type(basedate))
  formatfrom="%Y-%m-%dT%H:%M:%Sz"
  formatto="%H:%M:%S"
  last_time=datetime.strptime(basedate,formatfrom).strftime(formatto)
  print("Current time: ",current_time)
  print("Last Time: ",last_time)
  FMT = '%H:%M:%S'
  tdelta = datetime.strptime(current_time,FMT)- datetime.strptime(last_time,FMT)
  print("tdelta")
  print(type(str(tdelta)))
  print(type(last_time))
  #=datetime.datetime.strptime(last_time,"%H")
  #rint("b: ",b)
  list1=[]
  def Convert(string):
    li = list(string.split(":")) 
    return li
  list1=(Convert(str(tdelta)))
  print(list1)
  print(type(list1[0]))
  li=[]
  li=list(list1[0].split(" "))
  print(li)
  list1.insert(0,li)
  del list1[1]
  print("LIST1: ",list1[0][0])
  if ('day' in list1[0]):
     print("Day Present")
  else:
    list1[0].insert(0,'0')
    list1[0].insert(1,'day,')
    print("Update list:",list1)
    
  print("list1",list1)  
  total_minute=(int(list1[0][0])*(-1)*24+int(list1[0][2]))*60+int(list1[1])
  print("Total Minute: ",total_minute)
 
  
  if(total_minute<=30):
    b=max(t,key=t.count)
    print("maximum data ",max(t,key=t.count)) 
    URl='https://api.thingspeak.com/update?api_key='
    KEY='B9RDBVP7MF9JYNEV'
    HEADER='&field1={}&field2={}'.format(b,b)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)


if __name__ == '__main__':
    
  read_data_thingspeak()
  #hingspeak_post()
