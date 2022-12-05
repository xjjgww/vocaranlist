#!/bin/bash

python3.9 makejson.py
echo
python3.9 listuta.py # slow
echo
python3.9 fixlistuta.py
echo
python3.9 songdb.py # slow
echo

