#!/bin/bash

set -x

SOUFOLDER="../json/"
DESFOLDER="../js/"

cp $SOUFOLDER/songlist_fix.json $DESFOLDER/songlist.js
sed -i '1s/^/var songjsonobj = /g' $DESFOLDER/songlist.js
echo ";" >> $DESFOLDER/songlist.js

cp $SOUFOLDER/episodelist.json $DESFOLDER/episodelist.js
sed -i '1s/^/var episodejsonobj = /g' $DESFOLDER/episodelist.js
echo ";" >> $DESFOLDER/episodelist.js

cp $SOUFOLDER/songdb.json $DESFOLDER/songdblist.js
sed -i '1s/^/var songdbjsonobj = /g' $DESFOLDER/songdblist.js
echo ";" >> $DESFOLDER/songdblist.js

set +x
