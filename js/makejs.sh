#!/bin/bash

set -x

cp ../json/songlist_fix.json songlist.js
songsuffix='`;
var songjsonobj = JSON.parse(songlistjson);
'
sed -i '1i\var songlistjson = `' songlist.js
echo $songsuffix >> songlist.js

cp ../json/episodelist.json episodelist.js
episodesuffix='`;
var episodejsonobj = JSON.parse(episodelistjson);
'
sed -i '1i\var episodelistjson = `' episodelist.js
echo $episodesuffix >> episodelist.js

cp ../json/songdb.json songdblist.js
songdbsuffix='`;
var songdbjsonobj = JSON.parse(songdblistjson);
'
sed -i '1i\var songdblistjson = `' songdblist.js
echo $songdbsuffix >> songdblist.js

set +x
