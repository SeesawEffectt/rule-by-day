import requests
import xmltodict
from datetime import datetime
from email.utils import parsedate_to_datetime

userin = int(input("Please input the number of days you would like to search back: "))
twentyfour = int(datetime.now().timestamp()) - 86400*userin
repetitions = 0
while True:
  response = requests.get(f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1000&pid={repetitions}")
  data = xmltodict.parse(response.content)
  if int(parsedate_to_datetime(data['posts']['post'][999]['@created_at']).timestamp()) <= twentyfour:
    lst = [(x['@id'], int(parsedate_to_datetime(x['@created_at']).timestamp())) for x in data['posts']['post']] 
    res = next((x for x in lst if x[1] <= twentyfour), None)
    print(f"Post ID: {res[0]}")
    print(f"Unix Timestamp: {res[1]}")
    print(f"Local: {datetime.fromtimestamp(res[1])}")
    break
  repetitions += 1
  print(f"{repetitions*1000} posts loaded...")
