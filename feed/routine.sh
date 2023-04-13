#!/bin/bash

python3 makejson.py
echo
python3 listuta.py # slow
echo
python3 fixlistuta.py
echo
python3 songdb.py # slow
echo

