import json
import requests
import re
import sys

print('''\033[33;1m
########################
#       Get rss        #
########################
\033[0m''')

ssmm = 'sm37357711'
if len(sys.argv) > 1: ssmm = sys.argv[1]

# parse
print("\033[32;7m"+ssmm+"\033[0m")
sm = ssmm
url = 'http://nicodb.jp/u/index.php/bgm/rankrss/'+sm
print(url)
readweb = requests.get(url).text
print(readweb)
