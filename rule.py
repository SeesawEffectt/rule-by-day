import requests
import xmltodict
from datetime import datetime
from email.utils import parsedate_to_datetime

twentyfour = int(datetime.now().timestamp()) - 86400*1
repetitions = 0
while True:
  response = requests.get(f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1000&pid={repetitions}")
  data = xmltodict.parse(response.content)
  if int(parsedate_to_datetime(data['posts']['post'][999]['@created_at']).timestamp()) <= twentyfour:
    print(data['posts']['post'][999]['@id'])
    break
  repetitions += 1
