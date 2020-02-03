#!/bin/bash

set -x

cp ../json/songlist_fix.json songlist.js
sed -i '1s/^/var songjsonobj = /g' songlist.js
echo ";" >> songlist.js

cp ../json/episodelist.json episodelist.js
sed -i '1s/^/var episodejsonobj = /g' episodelist.js
echo ";" >> episodelist.js

cp ../json/songdb.json songdblist.js
sed -i '1s/^/var songdbjsonobj = /g' songdblist.js
echo ";" >> songdblist.js

set +x
