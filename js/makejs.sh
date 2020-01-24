#!/bin/bash

set -x

cp ../json/songlist.json songlist.js
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

set +x
