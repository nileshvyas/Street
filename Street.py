import urllib.request
import requests
import threading
import jsonlib




# Define a function that will post on server every 15 Seconds  
  
def read_data_thingspeak():
  threading.Timer(15,read_data_thingspeak).start()
  URL=' https://api.thingspeak.com/channels/538984/feeds.json?api_key='
  KEY='X34X42TNNLBL2J21'
  HEADER='&results=10'
  NEW_URL=URL+KEY+HEADER
  print(NEW_URL)

  get_data=requests.get(NEW_URL).json()
  print(get_data)
  channel_id=get_data['channel']['id']

  feild_1=get_data['feeds']
  print("field_1 :")
  print(feild_1)

  t=[]
  for x in feild_1:
    #print(x['field1'])
    t.append(x['field1'])
    a=x['field1']
    print('a=',a)

  #def thingspeak_post(self):
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
