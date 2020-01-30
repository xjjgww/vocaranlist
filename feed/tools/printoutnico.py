from requests_html import HTMLSession
session = HTMLSession()
import json
import re

# rr = session.get('https://www.nicovideo.jp/watch/sm36237863')
rr = session.get('https://www.nicovideo.jp/watch/sm36153076')
print(rr.html.find('#js-initial-watch-data'))

dataapiraw = rr.html.find('#js-initial-watch-data')[0].attrs['data-api-data'] # str
# print(dataapiraw)
dataapi = re.sub(r"\"description\".+?\"thumbnailURL\"", "\"thumbnailURL\"", dataapiraw)

# print(dataapi)
jvideo = json.loads(dataapi)['video'] # dict
jowner = json.loads(dataapi)['owner'] # dict

jvideo_str = json.dumps(jvideo, indent=2) # str
jowner_str = json.dumps(jowner, indent=2) # str

print(jvideo_str)
print(jowner_str)

# print(json.dumps(jowner, indent=2, ensure_ascii=False))

