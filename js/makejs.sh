#!/bin/bash

set -x

cp ../json/songlist.json songlist.js
suffix='`;
var songjsonobj = JSON.parse(songlistjson);
'
sed -i '1i\var songlistjson = `' songlist.js
echo $suffix >> songlist.js

set +x
