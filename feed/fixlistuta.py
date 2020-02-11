import re
import json
from bs4 import BeautifulSoup

with open('../json/songlist.json') as json_file:
    data = json.load(json_file)
    for sm in data:
        smnumber = int(sm.replace("sm", ""))
        tag = 2
        if smnumber > 35323499: tag = 0
        if smnumber > 35104863 and smnumber <= 35323499: tag = 1

        if tag > 1: continue
        print(sm)
        rawdict = data[sm]
        ii = len(rawdict)-1
        utarank = 10
        while ii >= 0:
            if ii == (len(rawdict)-1):
                rawdict[ii]['title'] = re.sub(r'.+\uff1a', 'Ending\uff1a', rawdict[ii]['title'], 1)
            elif utarank >= 1:
                rawdict[ii]['title'] = re.sub(r'.+\uff1a', 'UTAU'+str(utarank)+'\u4f4d\uff1a', rawdict[ii]['title'], 1)
                utarank -= 1
            if tag==0:
                if re.search(r'^[23][^0]\u4f4d\uff1a', rawdict[ii]['title']):
                    rawdict.pop(ii)
            elif tag==1 and utarank==0:
                rawdict[ii-1]['title'] = re.sub(r'.+\uff1a', 'Pick Up\uff1a', rawdict[ii-1]['title'], 1)
                utarank -=1
            ii -= 1

with open('../json/songlist_fix.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
